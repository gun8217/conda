import numpy as np

# 데이터를 정의합니다.
data = [
    {'type': 'chapparal', 'stream': False, 'slope': 'steep', 'elevation': 'high'},
    {'type': 'riparian', 'stream': True, 'slope': 'moderate', 'elevation': 'low'},
    {'type': 'riparian', 'stream': True, 'slope': 'steep', 'elevation': 'medium'},
    {'type': 'chapparal', 'stream': False, 'slope': 'steep', 'elevation': 'medium'},
    {'type': 'connifer', 'stream': False, 'slope': 'flat', 'elevation': 'high'},
    {'type': 'connifer', 'stream': True, 'slope': 'steep', 'elevation': 'highest'},
    {'type': 'chapparal', 'stream': True, 'slope': 'steep', 'elevation': 'high'}
]

# 각 식생 타입의 비율을 계산합니다.
types = [entry['type'] for entry in data]
unique_types, counts = np.unique(types, return_counts=True)
total_count = len(data)
proportions = counts / total_count

# 부모 노드 엔트로피를 계산합니다.
def entropy(probs):
    return -np.sum(probs * np.log2(probs + np.finfo(float).eps))

parent_entropy = entropy(proportions)
print(f"Parent entropy: {parent_entropy:.4f}")
