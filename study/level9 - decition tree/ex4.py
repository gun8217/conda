import numpy as np


def entropy(probs):
    return -np.sum(p * np.log2(p) if p > 0 else 0 for p in probs)


def calculate_entropy_for_feature(data, feature):
    feature_values = [entry[feature] for entry in data]
    feature_value_counts = {}
    
    for value in np.unique(feature_values):
        subset = [entry for entry in data if entry[feature] == value]
        subset_types = [entry['type'] for entry in subset]
        unique_subset_types, subset_counts = np.unique(subset_types, return_counts=True)
        subset_proportions = subset_counts / len(subset)
        entropy_value = entropy(subset_proportions)
        feature_value_counts[value] = (len(subset) / len(data), entropy_value)
    
    return feature_value_counts


def information_gain(parent_entropy, feature_value_counts):
    weighted_entropy_sum = np.sum([weight * entropy for weight, entropy in feature_value_counts.values()])
    return parent_entropy - weighted_entropy_sum


data = [
    {'type': 'chapparal', 'stream': False, 'slope': 'steep', 'elevation': 'high'},
    {'type': 'riparian', 'stream': True, 'slope': 'moderate', 'elevation': 'low'},
    {'type': 'riparian', 'stream': True, 'slope': 'steep', 'elevation': 'medium'},
    {'type': 'chapparal', 'stream': False, 'slope': 'steep', 'elevation': 'medium'},
    {'type': 'connifer', 'stream': False, 'slope': 'flat', 'elevation': 'high'},
    {'type': 'connifer', 'stream': True, 'slope': 'steep', 'elevation': 'highest'},
    {'type': 'chapparal', 'stream': True, 'slope': 'steep', 'elevation': 'high'}
]

types = [entry['type'] for entry in data]
unique_types, counts = np.unique(types, return_counts=True)
total_count = len(data)
proportions = counts / total_count

# 부모 노드 엔트로피 계산
parent_entropy = entropy(proportions)
print(parent_entropy)

# Calculate entropy for 'stream'
stream_entropy = calculate_entropy_for_feature(data, 'stream')
stream_ig = information_gain(parent_entropy, stream_entropy)
print(f"Information Gain for 'stream': {stream_ig:.4f}")

# Calculate entropy for 'slope'
slope_entropy = calculate_entropy_for_feature(data, 'slope')
slope_ig = information_gain(parent_entropy, slope_entropy)
print(f"Information Gain for 'slope': {slope_ig:.4f}")

# Calculate entropy for 'elevation'
elevation_entropy = calculate_entropy_for_feature(data, 'elevation')
elevation_ig = information_gain(parent_entropy, elevation_entropy)
print(f"Information Gain for 'elevation': {elevation_ig:.4f}")
print()

features = ['stream', 'slope', 'elevation']

for feature in features:
    feature_entropy = calculate_entropy_for_feature(data, feature)
    feature_ig = information_gain(parent_entropy, feature_entropy)
    print(f"Information Gain for '{feature}': {feature_ig:.4f}")