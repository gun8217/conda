import numpy as np
import matplotlib.pyplot as plt

# 무게중심을 random하게 만들고, dataset의 모양이 (100, 2)이 되도록 만들기 scatter plot으로 시각화하기
n_data = 100

centroid = np.random.uniform(low=-10, high=10, size=(2,))

data = np.random.normal(loc=centroid, scale=1, size=(n_data, 2))

fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(data[:, 0], data[:, 1], alpha=0.6)
ax.scatter(centroid[0], centroid[1], color='red', marker='x', s=100)

fig.tight_layout()
plt.show()