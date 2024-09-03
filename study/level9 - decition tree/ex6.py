import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# 데이터 정의
data = [
    {'type': 'chapparal', 'stream': False, 'slope': 'steep', 'elevation': 'high'},
    {'type': 'riparian', 'stream': True, 'slope': 'moderate', 'elevation': 'low'},
    {'type': 'riparian', 'stream': True, 'slope': 'steep', 'elevation': 'medium'},
    {'type': 'chapparal', 'stream': False, 'slope': 'steep', 'elevation': 'medium'},
    {'type': 'connifer', 'stream': False, 'slope': 'flat', 'elevation': 'high'},
    {'type': 'connifer', 'stream': True, 'slope': 'steep', 'elevation': 'highest'},
    {'type': 'chapparal', 'stream': True, 'slope': 'steep', 'elevation': 'high'}
]

# 데이터프레임 생성
df = pd.DataFrame(data)

# 라벨 인코딩
label_encoders = {}
for column in df.columns:
    if df[column].dtype == object:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

X = df.drop('type', axis=1)
y = df['type']

# 엔트로피 계산 함수
def entropy(probabilities):
    return -np.sum(prob * np.log2(prob) if prob > 0 else 0 for prob in probabilities)

# 전체 엔트로피
total_counts = y.value_counts()
total_entropy = entropy(total_counts / len(y))

# 특성별 엔트로피 계산
def feature_entropy(feature):
    feature_values = X[feature]
    entropies = []
    for value in feature_values.unique():
        subset = y[feature_values == value]
        counts = subset.value_counts()
        entropies.append(entropy(counts / len(subset)))
    weighted_entropy = np.sum(
        (len(subset) / len(y)) * entropy(counts / len(subset))
        for value in feature_values.unique()
        for subset in [y[feature_values == value]]
        if len(subset) > 0
    )
    return weighted_entropy

# 정보 이득 계산
def information_gain(feature):
    return total_entropy - feature_entropy(feature)

# 각 특성의 정보 이득 계산
features = X.columns
info_gains = {feature: information_gain(feature) for feature in features}

# 결과 출력
print(f"Total Entropy: {total_entropy:.4f}")
for feature, gain in info_gains.items():
    print(f"Information Gain for '{feature}': {gain:.4f}")

# 노드 선택
best_feature = max(info_gains, key=info_gains.get)
print(f"The best feature to split on is '{best_feature}'")


import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# 결정 트리 모델 학습
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf.fit(X, y)

# 트리 시각화
plt.figure(figsize=(20, 10))
plot_tree(clf, feature_names=X.columns, class_names=label_encoders['type'].classes_, filled=True, rounded=True)
plt.title("Decision Tree Visualization")
plt.show()
