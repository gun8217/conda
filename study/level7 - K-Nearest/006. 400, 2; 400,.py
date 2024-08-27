import numpy as np
import matplotlib.pyplot as plt

# 4개의 class(0, 1, 2, 3)를 가지는 dataset 만들기 : X: (400, 2),  y: (400,)
n_class = 4
n_data = 100

centroids = np.random.uniform(low=-10, high=10, size=(n_class, 2))

X_list = []; y_list = []
for i in range(n_class):
    X_ = np.random.normal(loc=centroids[i], scale=2, size=(n_data, 2))
    X_list.append(X_)
    y_list.append(np.full(n_data, i))

X = np.vstack(X_list)
y = np.hstack(y_list)

fig, ax = plt.subplots(figsize=(7, 7))
cmap = plt.get_cmap('tab10')
colors = [cmap(i) for i in range(n_class)]

for i in range(n_class):
    ax.scatter(X[y == i][:, 0], X[y == i][:, 1], color=colors[i], alpha=0.6)

ax.scatter(centroids[:, 0], centroids[:, 1], color='black', marker='x', linewidth=2, s=100)

fig.tight_layout()
plt.show()