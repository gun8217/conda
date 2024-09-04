from utils import *

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import _tree

# 데이터셋
data = [
    {'Vegetation': 'chaparral', 'Stream': False, 'Slope': 'steep', 'Elevation': 'high'},
    {'Vegetation': 'riparian', 'Stream': True, 'Slope': 'moderate', 'Elevation': 'low'},
    {'Vegetation': 'riparian', 'Stream': True, 'Slope': 'steep', 'Elevation': 'medium'},
    {'Vegetation': 'chaparral', 'Stream': False, 'Slope': 'steep', 'Elevation': 'medium'},
    {'Vegetation': 'conifer', 'Stream': False, 'Slope': 'flat', 'Elevation': 'high'},
    {'Vegetation': 'conifer', 'Stream': True, 'Slope': 'steep', 'Elevation': 'highest'},
    {'Vegetation': 'chaparral', 'Stream': True, 'Slope': 'steep', 'Elevation': 'high'}
]

df = pd.DataFrame(data)

# 라벨 인코딩
label_encoders = {}
for column in df.columns:
    if df[column].dtype == 'object':
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

X = df.drop('Vegetation', axis=1)
y = df['Vegetation']

# 결정 트리 학습
clf = DecisionTreeClassifier()
clf.fit(X, y)

# 모델의 내부 속성 확인
tree_ = clf.tree_
feature_names = X.columns
feature_name = [
    feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
    for i in tree_.feature
]

# 각 노드의 정보 출력
for i in range(tree_.node_count):
    print(f"Node {i}:")
    print(f"  Feature: {feature_name[i]}")
    print(f"  Threshold: {tree_.threshold[i]}")
    print(f"  Value: {tree_.value[i]}")
    print(f"  Left child: {tree_.children_left[i]}")
    print(f"  Right child: {tree_.children_right[i]}")
    print()
