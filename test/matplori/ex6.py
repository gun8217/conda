# 연습 문제 6: 비대칭 분포 데이터 생성
# 목표: 비대칭적인 데이터를 생성하고 시각화하세요.
# 한 클래스는 정규 분포를 따르는 데이터를 생성합니다.
# 다른 클래스는 지수 분포를 따르며, 특정 방향으로 긴 꼬리를 가진 데이터를 생성합니다.
# 각 클래스에 대해 200개의 데이터 포인트를 생성하세요.
# 두 클래스를 서로 다른 색으로 구분하여 시각화하세요.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

data1 = np.random.normal(loc=0, scale=1, size=1000)  # 정규분포 : 평균 0, 표준편차 1
data2 = np.random.uniform(low=-3, high=3, size=1000)  # -3에서 3까지 균등 분포
data3 = np.random.exponential(scale=1, size=1000)  # 평균 1인 지수 분포

plt.figure(figsize=(12, 6))

plt.hist(data1, bins=30, alpha=0.5, label='Normal')
plt.hist(data2, bins=30, alpha=0.5, label='Uniform')
plt.hist(data3, bins=30, alpha=0.5, label='Exponential')

plt.legend()


plt.tight_layout()
plt.show()