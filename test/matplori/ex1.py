# 연습 문제 1: 두 개의 원형 데이터 생성
# 목표: 두 개의 원형으로 분포하는 데이터를 생성하고 시각화하세요.
# 각각의 원은 다른 반지름을 가지며, 중심점은 임의로 설정됩니다.
# 각 원에 대해 100개의 데이터 포인트를 생성하세요.
# 데이터 포인트는 중심점에서 일정한 반지름 내에서 균일하게 분포하도록 합니다.
# 각 원의 데이터 포인트를 다른 색으로 구분하여 시각화하세요.

import numpy as np
import matplotlib.pyplot as plt

n_data = 100  # 각 원형의 데이터 포인트 수
radius = [5, 10]  # 원의 반지름 리스트
centers = [np.array([0, 0]), np.array([15, 15])]  # 중심점 리스트
colors = ['blue', 'red']  # 색상 리스트


fig, ax = plt.subplots(figsize=(7, 7))

for i in range(len(radius)):
    angles = np.random.uniform(0, 2 * np.pi, n_data)
    radii_values = np.random.uniform(0, radius[i], n_data)
    x = centers[i][0] + radii_values * np.cos(angles)
    y = centers[i][1] + radii_values * np.sin(angles)
    data = np.column_stack((x, y))

    ax.scatter(data[:, 0], data[:, 1], color=colors[i], alpha=0.5, label=f'Circle {i+1}')

ax.set_aspect('equal') # x, y축 비율 동일하게 설정
ax.legend()


fig.tight_layout()
plt.show()