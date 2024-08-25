# 연습 문제 4: 나선형 데이터 생성
# 목표: 두 개의 나선형으로 분포하는 데이터를 생성하고 시각화하세요.
# 첫 번째 클래스는 r=a⋅θ 형태의 나선을 중심으로 분포하는 데이터를 생성합니다.
# 두 번째 클래스는 반대 방향으로 회전하는 나선을 중심으로 분포하는 데이터를 생성합니다.
# 각 클래스에 대해 100개의 데이터 포인트를 생성하세요.
# 각 나선의 시작점을 달리하여 두 클래스가 서로 얽히도록 만듭니다.

import numpy as np
import matplotlib.pyplot as plt

n_data = 100  # 각 나선에 생성할 데이터 포인트 수
n_spirals = 2  # 나선의 개수 (2개로 설정)
noise = 0.5  # 노이즈 크기
turns = 20  # 나선의 회전 수
colors = ['blue', 'red']  # 나선의 색상 리스트

plt.figure(figsize=(7, 7))

for i in range(n_spirals):
    theta = np.linspace(0, turns * 2 * np.pi, n_data)
    r = np.linspace(0, 10, n_data)
    x = r * np.cos(theta + i * np.pi) + np.random.normal(0, noise, n_data)
    y = r * np.sin(theta + i * np.pi) + np.random.normal(0, noise, n_data)
    
    plt.scatter(x, y, color=colors[i], label=f'Spiral {i + 1}')
    
plt.legend()

plt.tight_layout()
plt.show()