import numpy as np

# 클래스와 특성 데이터
classes = np.array(['ch', 'ri', 'ch', 'co', 'ch'])
features = np.array(['h', 'm', 'm', 'hi', 'h'])

# 부모 노드의 클래스 분포
unique_classes, class_counts = np.unique(classes, return_counts=True)
class_probabilities = class_counts / class_counts.sum()

# 부모 노드 엔트로피
parent_entropy = -np.sum(class_probabilities * np.log2(class_probabilities))
print(f'Parent Node Entropy: {parent_entropy}')

# 자식 노드 분포
stream_h_classes = classes[features == 'h']
stream_m_classes = classes[features == 'm']
stream_hi_classes = classes[features == 'hi']

# 각 자식 노드의 클래스 분포
unique_classes_h, class_counts_h = np.unique(stream_h_classes, return_counts=True)
unique_classes_m, class_counts_m = np.unique(stream_m_classes, return_counts=True)
unique_classes_hi, class_counts_hi = np.unique(stream_m_classes, return_counts=True)

class_probabilities_h = class_counts_h / class_counts_h.sum()
class_probabilities_m = class_counts_m / class_counts_m.sum()
class_probabilities_hi = class_counts_hi / class_counts_hi.sum()

# 자식 노드의 엔트로피
entropy_h = -np.sum(class_probabilities_h * np.log2(class_probabilities_h))
entropy_m = -np.sum(class_probabilities_m * np.log2(class_probabilities_m))
entropy_hi = -np.sum(class_probabilities_hi * np.log2(class_probabilities_hi))

# 자식 노드 비율
proportion_h = len(stream_h_classes) / len(classes)
proportion_m = len(stream_m_classes) / len(classes)
proportion_hi = len(stream_hi_classes) / len(classes)

# 정보 이득(IG) 계산
weighted_entropy_h = proportion_h * entropy_h
weighted_entropy_m = proportion_m * entropy_m
weighted_entropy_hi = proportion_hi * entropy_hi
information_gain = parent_entropy - (weighted_entropy_h + weighted_entropy_m + weighted_entropy_hi)

print(f'Information Gain (IG): {information_gain}')
