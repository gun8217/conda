import numpy as np

# 클래스와 특성 데이터
classes = np.array(['ch', 'ri', 'ch', 'co', 'ch'])
features = np.array(['F', 'T', 'F', 'T', 'T'])

# 부모 노드의 클래스 분포
unique_classes, class_counts = np.unique(classes, return_counts=True)
class_probabilities = class_counts / class_counts.sum()

# 부모 노드 엔트로피
parent_entropy = -np.sum(class_probabilities * np.log2(class_probabilities))
print(f'Parent Node Entropy: {parent_entropy}')

# 자식 노드 분포
stream_F_classes = classes[features == 'F']
stream_T_classes = classes[features == 'T']

# 각 자식 노드의 클래스 분포
unique_classes_F, class_counts_F = np.unique(stream_F_classes, return_counts=True)
unique_classes_T, class_counts_T = np.unique(stream_T_classes, return_counts=True)
print(unique_classes_F, class_counts_F)
print(unique_classes_T, class_counts_T)

class_probabilities_F = class_counts_F / class_counts_F.sum()
class_probabilities_T = class_counts_T / class_counts_T.sum()

# 자식 노드의 엔트로피
entropy_F = -np.sum(class_probabilities_F * np.log2(class_probabilities_F))
entropy_T = -np.sum(class_probabilities_T * np.log2(class_probabilities_T))

# 자식 노드 비율
proportion_F = len(stream_F_classes) / len(classes)
proportion_T = len(stream_T_classes) / len(classes)

# 정보 이득(IG) 계산
weighted_entropy_F = proportion_F * entropy_F
weighted_entropy_T = proportion_T * entropy_T
information_gain = parent_entropy - (weighted_entropy_F + weighted_entropy_T)

print(f'Information Gain (IG): {information_gain}')
