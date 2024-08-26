import numpy as np
import matplotlib.pyplot as plt

n_data = 100
n_class = 4
cmap = plt.get_cmap('tab10')
colors = [cmap(i) for i in range(n_class)]

data, centroids = [], []
for _ in range(n_class):
    centroid = np.random.uniform(low=-10, high=10, size=(2,))
    data_ = np.random.normal(loc=centroid, scale=1, size=(n_data, 2))
    centroids.append(centroid)
    data.append(data_)

centroids = np.vstack([centroid])
data = np.vstack(data)
print(centroids.shape, data.shape)

# fig, ax = plt.subplots(figsize=(5, 5))
# for class_idx in range(n_class):
#     data_ = data[class_idx * n_data : (class_idx + 1) * n_data]
#     ax.scatter(data_[:, 0], data_[:, 1], alpha=0.5)

# for centroid in centroids:
#     ax.scatter(centroid[1], centroid[1], c="purple", marker='x', s=100)

# fig.tight_layout()
# plt.show()