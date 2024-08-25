# 연습 문제 2: 두 클래스가 섞인 선형 데이터
# 목표: 두 클래스가 선형적으로 분리된 데이터를 생성하고 시각화하세요.
# 첫 번째 클래스는 y=x+5를 중심으로 분포하는 데이터를 생성합니다.
# 두 번째 클래스는 y=x−5를 중심으로 분포하는 데이터를 생성합니다.
# 각 클래스에 대해 50개의 데이터 포인트를 생성하세요.
# 노이즈를 추가하여 두 클래스 간의 일부 데이터가 섞이도록 만듭니다.

import numpy as np
import matplotlib.pyplot as plt

n_data = 50  # 각 클래스에 생성할 데이터 포인트 수
slopes = [1, 1]  # 기울기 리스트 (여기서는 동일한 기울기)
intercepts = [5, -5]  # y절편 리스트
colors = ['blue', 'red']  # 색상 리스트
noise_level = 2  # 노이즈 크기


fig, ax = plt.subplots(figsize=(7, 7))

for i in range(len(intercepts)):
    x = np.random.uniform(-10, 10, n_data)
    y = slopes[i] * x + intercepts[i] + np.random.normal(0, noise_level, n_data)
    data = np.column_stack((x, y))
    
    ax.scatter(data[:, 0], data[:, 1], color=colors[i], label=f'Class {i+1}')

ax.legend()


fig.tight_layout()
plt.show()