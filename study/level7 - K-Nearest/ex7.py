import numpy as np
import matplotlib.pyplot as plt

n_data = 100
n_class = 4
cmap = plt.get_cmap('tab10')
colors = [cmap(i) for i in range(n_class)]

fig, ax = plt.subplots(figsize=(7, 7))

centroids = []
for class_idx in range(n_class):
    centroid = np.random.uniform(-10, 10, (2,))
    centroids.append(centroid)
    data = np.random.normal(centroid, 1, (n_data, 2))
    ax.scatter(centroid[0], centroid[1],
               s=100,
               c='black',
               marker='x')
    ax.scatter(data[:, 0], data[:, 1],
               facecolor='None',
               alpha=0.5,
               edgecolor=colors[class_idx])


fig.tight_layout()
plt.show()