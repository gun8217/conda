# 연습 문제 5: 군집 데이터 생성
# 목표: 세 개의 군집(clusters)을 가진 데이터를 생성하고 시각화하세요.
# 각 군집의 중심점은 임의로 설정하세요.
# 각 군집의 데이터는 중심점 주위에 정규 분포로 생성됩니다.
# 한 군집은 다른 군집에 비해 더 넓게 퍼져 있도록 만듭니다.
# 각 군집에 대해 100개의 데이터 포인트를 생성하세요.
# 각 군집을 다른 색으로 구분하여 시각화하세요.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 문제 1: 원형 분포 데이터
def generate_circle_data(n_data, radius, noise, center):
    theta = np.linspace(0, 2 * np.pi, n_data)
    x = center[0] + radius * np.cos(theta) + np.random.normal(0, noise, n_data)
    y = center[1] + radius * np.sin(theta) + np.random.normal(0, noise, n_data)
    return x, y

# 문제 2: 선형 분포 데이터
def generate_line_data(n_data, slope, intercept, noise):
    x = np.linspace(-10, 10, n_data)
    y = slope * x + intercept + np.random.normal(0, noise, n_data)
    return x, y

# 문제 3: 3차원 군집 데이터
def generate_cluster_data(n_data, centers, cluster_spread):
    cluster_data = []
    for center in centers:
        cluster_data.append(center + cluster_spread * np.random.randn(n_data, 3))
    return np.vstack(cluster_data)

# 문제 4: 나선형 데이터
def generate_spiral_data(n_data, turns, noise, offset=0):
    theta = np.linspace(0, turns * 2 * np.pi, n_data)
    r = np.linspace(0, 10, n_data)
    x = r * np.cos(theta + offset) + np.random.normal(0, noise, n_data)
    y = r * np.sin(theta + offset) + np.random.normal(0, noise, n_data)
    return x, y


plt.figure(figsize=(7, 7))

# 문제 1: 원형 데이터
x1, y1 = generate_circle_data(100, 5, 0.5, center=[-10, 10])
plt.scatter(x1, y1, color='blue', label='Circle')

# 문제 2: 선형 데이터
x2, y2 = generate_line_data(100, 1, 0, 0.5)
plt.scatter(x2, y2, color='green', label='Line')

# 문제 4: 나선형 데이터 (2개)
x3, y3 = generate_spiral_data(100, 3, 0.5)
plt.scatter(x3, y3, color='red', label='Spiral 1')

x4, y4 = generate_spiral_data(100, 3, 0.5, offset=np.pi)
plt.scatter(x4, y4, color='orange', label='Spiral 2')

plt.legend()


plt.tight_layout()
plt.show()


# 문제 3: 3차원 군집 데이터
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
centers = np.array([[5, 5, 5], [-5, -5, -5]])
cluster_data = generate_cluster_data(100, centers, 1.5)
ax.scatter(cluster_data[:, 0], cluster_data[:, 1], cluster_data[:, 2], color='purple', label='Clusters')

ax.legend()

fig.tight_layout()
plt.show()