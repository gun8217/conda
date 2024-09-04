import numpy as np

# 데이터 준비 (예: 2D 데이터와 레이블)
X = np.array([[2, 3], [10, 15], [7, 8], [3, 4], [6, 7]])
y = np.array([0, 1, 1, 0, 1])  # 0 또는 1로 클래스 레이블

# 엔트로피 계산 함수 : 정보와 확률은 반비례
# ex) 1/8 정보량 = -log2 * 1/8 = 3bit
# 정보량의 기대값 : 가중평균
def entropy(y):
    classes, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    return -np.sum(probabilities * np.log2(probabilities))

# 데이터 분할 함수
def split_dataset(X, y, feature_idx, threshold):
    left_mask = X[:, feature_idx] <= threshold
    right_mask = X[:, feature_idx] > threshold
    return X[left_mask], y[left_mask], X[right_mask], y[right_mask]

# 정보 이득 계산 함수
def information_gain(X, y, feature_idx, threshold):
    left_X, left_y, right_X, right_y = split_dataset(X, y, feature_idx, threshold)
    p_left = len(left_y) / len(y)
    p_right = len(right_y) / len(y)
    return entropy(y) - (p_left * entropy(left_y) + p_right * entropy(right_y))

# 트리 노드 분할
def best_split(X, y):
    best_gain = 0
    best_feature = None
    best_threshold = None
    for feature_idx in range(X.shape[1]):
        thresholds = np.unique(X[:, feature_idx])
        for threshold in thresholds:
            gain = information_gain(X, y, feature_idx, threshold)
            if gain > best_gain:
                best_gain = gain
                best_feature = feature_idx
                best_threshold = threshold
    return best_feature, best_threshold

# 트리 학습
def build_tree(X, y, depth=0, max_depth=2):
    if len(np.unique(y)) == 1:
        return {'label': y[0]}
    if depth >= max_depth:
        return {'label': np.bincount(y).argmax()}
    
    feature, threshold = best_split(X, y)
    if feature is None:
        return {'label': np.bincount(y).argmax()}
    
    left_X, left_y, right_X, right_y = split_dataset(X, y, feature, threshold)
    return {
        'feature': feature,
        'threshold': threshold,
        'left': build_tree(left_X, left_y, depth + 1, max_depth),
        'right': build_tree(right_X, right_y, depth + 1, max_depth)
    }

# 트리 예측
def predict(tree, X):
    if 'label' in tree:
        return tree['label']
    if X[tree['feature']] <= tree['threshold']:
        return predict(tree['left'], X)
    else:
        return predict(tree['right'], X)

# 트리 생성 및 예측
tree = build_tree(X, y)
print(tree)

# 예측
test_sample = np.array([5, 7])
print("Prediction:", predict(tree, test_sample))
