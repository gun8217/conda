import numpy as np


def entropy(column):
    """Calculate the entropy of a column."""
    values, counts = np.unique(column, return_counts=True)
    probabilities = counts / counts.sum()
    return -np.sum(probabilities * np.log2(probabilities + 1e-9))

def weighted_entropy(df, feature, target):
    """Calculate the weighted entropy of a feature."""
    feature_values = df[feature].unique()
    weighted_entropy = 0.0
    total_count = len(df)
    
    for value in feature_values:
        subset = df[df[feature] == value]
        weight = len(subset) / total_count
        entropy_value = entropy(subset[target])
        weighted_entropy += weight * entropy_value
    
    return weighted_entropy

def information_gain(df, feature, target):
    """Calculate the information gain of a feature."""
    total_entropy = entropy(df[target])
    feature_entropy = weighted_entropy(df, feature, target)
    return total_entropy - feature_entropy

def split_data(df, feature):
    """Split data based on the values of a feature."""
    split_data_dict = {}
    feature_values = df[feature].unique()
    
    for value in feature_values:
        split_data_dict[value] = df[df[feature] == value]
    
    return split_data_dict

def build_tree(df, target, features):
    """Build the decision tree recursively."""
    # Check if all target values are the same
    if len(df[target].unique()) == 1:
        return df[target].iloc[0]
    
    # Check if no features left to split on
    if not features:
        return df[target].mode().iloc[0]
    
    # Calculate information gain for each feature
    gains = {feature: information_gain(df, feature, target) for feature in features}
    best_feature = max(gains, key=gains.get)
    
    # Create a new tree node
    tree = {best_feature: {}}
    
    # Split data on the best feature and build subtrees
    split_data_dict = split_data(df, best_feature)
    
    for value, subset in split_data_dict.items():
        subtree_features = [f for f in features if f != best_feature]
        subtree = build_tree(subset, target, subtree_features)
        tree[best_feature][value] = subtree
    
    return tree