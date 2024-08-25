# 연습 문제 3: 세 개의 서로 다른 분포 데이터
# 목표: 세 개의 다른 확률 분포를 가진 데이터를 생성하고 시각화하세요.
# 첫 번째 클래스는 평균이 0이고 표준편차가 1인 2차원 정규 분포를 따르는 데이터를 생성합니다.
# 두 번째 클래스는 균일 분포에서 데이터를 생성하여 정사각형 영역 내에 위치시킵니다.
# 세 번째 클래스는 지수 분포에서 데이터를 생성하여 음이 아닌 값만 가지는 데이터를 만듭니다.
# 각 클래스에 대해 200개의 데이터 포인트를 생성하세요.
# 각 클래스의 데이터를 다른 색으로 구분하여 시각화하세요.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n_data = 100  # 각 군집에 생성할 데이터 포인트 수
n_clusters = 4  # 군집의 개수
cluster_spread = 1.5  # 군집의 퍼짐 정도 (값이 클수록 퍼짐)
centers = np.random.uniform(-10, 10, (n_clusters, 3))  # 각 군집의 중심점 설정
colors = plt.cm.jet(np.linspace(0, 1, n_clusters))


fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection='3d')  # 3D 플롯 생성

for i in range(n_clusters):
    cluster_data = centers[i] + cluster_spread * np.random.randn(n_data, 3)
    
    ax.scatter(cluster_data[:, 0], cluster_data[:, 1], cluster_data[:, 2], 
               color=colors[i], label=f'Cluster {i+1}', alpha=0.6)

ax.legend()


fig.tight_layout()
plt.show()