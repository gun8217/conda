from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np

n_samples = 100

# 데이터 생성
X, y = make_blobs(n_samples=n_samples, centers=2, n_features=2, cluster_std=0.7)

# 로지스틱 회귀 모델 학습
model = LogisticRegression()
model.fit(X, y)

# 데이터 포인트 시각화
fig, ax = plt.subplots(figsize=(10, 10))
X_pos, X_neg = X[y == 1], X[y == 0]
ax.scatter(X_pos[:, 0], X_pos[:, 1], color='blue')
ax.scatter(X_neg[:, 0], X_neg[:, 1], color='red')

# 결정 경계 시각화
x_values = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
y_values = -(model.intercept_[0] + model.coef_[0][0] * x_values) / model.coef_[0][1]
ax.plot(x_values, y_values, color='green', linestyle='--')

# 축 설정
ax.tick_params(labelsize=15)
ax.set_xlabel('Feature 1', fontsize=15)
ax.set_ylabel('Feature 2', fontsize=15)

plt.show()
