import numpy as np
import matplotlib.pyplot as plt

# 4 class, class마다 100개의 점을 가지는 dataset 만들기 : (400, 2), class들의 centroid는 랜덤하게
n_class = 4
n_data = 100

centroids = np.random.uniform(low=-10, high=10, size=(n_class, 2))

data = []; labels = []
for i in range(n_class):
    class_data = np.random.normal(loc=centroids[i], scale=2, size=(n_data, 2))
    data.append(class_data)
    labels.append(np.full((n_data,), i))

data = np.vstack(data)
labels = np.hstack(labels)

fig, ax = plt.subplots(figsize=(7, 7))
cmap = plt.get_cmap('tab10')
colors = [cmap(i) for i in range(n_class)]

for i in range(n_class):
    ax.scatter(data[labels == i][:, 0], data[labels == i][:, 1], color=colors[i], alpha=0.6)

ax.scatter(centroids[:, 0], centroids[:, 1], color='black', marker='x', linewidth=2, s=100)

fig.tight_layout()
plt.show()