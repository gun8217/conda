from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 준비
# https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset/data
file_path = 'C:/Users/Administrator/Documents/conda/study/level8 - bayes/diabetes2.csv'
dia = pd.read_csv(file_path, index_col=0)
print(dia.head(), dia.shape)

X = dia[dia.columns[:-1]]
y = dia[dia.columns[-1]]


# 이상치 제거
from scipy import stats

# Z-score를 사용하여 이상치 탐지
z_scores = stats.zscore(X)
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
X_clean = X[filtered_entries]
y_clean = y[filtered_entries]

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.25,
                                                    shuffle=True,
                                                    random_state=42)

# 모델 훈련(knn, gusiann, decition 등의 모델을 바꿔 사용 가능?!)
decision_tree = DecisionTreeClassifier(criterion='entropy', random_state=32,
                                       min_samples_split=10, # 노드 분할 최소 샘플 수
                                       min_samples_leaf=5, # 리프 노드 최소 샘플 수
                                       max_depth=3) # 트리 최대 깊이
decision_tree.fit(X_train, y_train)

# 모델 평가
train_acc = decision_tree.score(X_train, y_train)
print("훈련 정확도 :", train_acc)

pred = decision_tree.predict(X_test) # 모델 테스트

test_acc = decision_tree.score(X_test, y_test)
print("테스트 정확도 :", test_acc)

cm = confusion_matrix(y_test, pred)
print(f"예측 결과 확인: {cm}")



for attr in dir(decision_tree):
    if not attr.startswith('__'):print(decision_tree)
    break
    
print(decision_tree.criterion)
print(decision_tree.feature_names_in_)
print(decision_tree.feature_importances_)



# from sklearn import tree

# plt.figure(figsize=(5, 10), dpi=300)
# tree.plot_tree(decision_tree,
#                feature_names=dia.columns[:-1],
#                impurity=True, filled=True,
#                rounded=True)

# plt.savefig('./dia_tree_entropy.png')
# plt.tight_layout()
# plt.show()


# ['Glucose'                         0.54564858
#  'BloodPressure'                   0.
#  'SkinThickness'                   0.
#  'Insulin'                         0.02165534
#  'BMI'                             0.23760352
#  'DiabetesPedigreeFunction'        0.
#  'Age'                             0.19509256]