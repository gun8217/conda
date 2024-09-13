import numpy as np
import matplotlib.pyplot as plt

# 평균이 (5, 3)이고 표준편차가 x, y방향으로 모두 1인 (100, 2) dataset 만들기
mean = [5, 3]
std_dev = 1
n_data = 100

data = np.random.normal(loc=mean, scale=std_dev, size=(n_data, 2))

fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(data[:, 0], data[:, 1], alpha=0.6)

fig.tight_layout()
plt.show()