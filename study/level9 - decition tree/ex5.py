import pandas as pd

# 데이터프레임 생성
data = [
    {'type': 'chapparal', 'stream': False, 'slope': 'steep', 'elevation': 'high'},
    {'type': 'riparian', 'stream': True, 'slope': 'moderate', 'elevation': 'low'},
    {'type': 'riparian', 'stream': True, 'slope': 'steep', 'elevation': 'medium'},
    {'type': 'chapparal', 'stream': False, 'slope': 'steep', 'elevation': 'medium'},
    {'type': 'connifer', 'stream': False, 'slope': 'flat', 'elevation': 'high'},
    {'type': 'connifer', 'stream': True, 'slope': 'steep', 'elevation': 'highest'},
    {'type': 'chapparal', 'stream': True, 'slope': 'steep', 'elevation': 'high'}
]

df = pd.DataFrame(data)
print(df)

# # 2. 데이터 시각화
# # 각 클래스별 분포
# import matplotlib.pyplot as plt
# import seaborn as sns

# # 클래스별 분포 시각화
# plt.figure(figsize=(8, 6))
# sns.countplot(x='type', data=df, palette='Set2')
# plt.title('Class Distribution')
# plt.xlabel('Type')
# plt.ylabel('Count')
# plt.show()

# # 각 속성에 대한 분포
# # 'stream'에 따른 클래스 분포
# plt.figure(figsize=(10, 6))
# sns.countplot(x='stream', hue='type', data=df, palette='Set2')
# plt.title('Class Distribution by Stream')
# plt.xlabel('Stream')
# plt.ylabel('Count')
# plt.show()

# # 'slope'에 따른 클래스 분포
# plt.figure(figsize=(10, 6))
# sns.countplot(x='slope', hue='type', data=df, palette='Set2')
# plt.title('Class Distribution by Slope')
# plt.xlabel('Slope')
# plt.ylabel('Count')
# plt.show()

# # 'elevation'에 따른 클래스 분포
# plt.figure(figsize=(10, 6))
# sns.countplot(x='elevation', hue='type', data=df, palette='Set2')
# plt.title('Class Distribution by Elevation')
# plt.xlabel('Elevation')
# plt.ylabel('Count')
# plt.show()

# # 3. 결정 트리 계산
# from sklearn.tree import DecisionTreeClassifier, export_text
# from sklearn.preprocessing import LabelEncoder

# # 라벨 인코딩
# label_encoders = {}
# for column in ['type', 'stream', 'slope', 'elevation']:
#     le = LabelEncoder()
#     df[column] = le.fit_transform(df[column])
#     label_encoders[column] = le

# # 피처와 타겟 설정
# X = df[['stream', 'slope', 'elevation']]
# y = df['type']

# # 결정 트리 모델 훈련
# clf = DecisionTreeClassifier(criterion='entropy')
# clf.fit(X, y)

# # 결정 트리 텍스트로 출력
# tree_rules = export_text(clf, feature_names=['stream', 'slope', 'elevation'])
# print(tree_rules)

# # 4. 결정 트리 시각화
# from sklearn import tree
# import graphviz

# # 결정 트리 시각화
# dot_data = tree.export_graphviz(clf, out_file=None, 
#                                 feature_names=['stream', 'slope', 'elevation'],  
#                                 class_names=label_encoders['type'].classes_,  
#                                 filled=True, rounded=True,  
#                                 special_characters=True)  
# graph = graphviz.Source(dot_data)  
# graph.render("decision_tree")  # 결정 트리를 'decision_tree.pdf'로 저장
# graph.view()  # 결정 트리 PDF 파일 열기