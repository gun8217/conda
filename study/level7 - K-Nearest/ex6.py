import numpy as np
import matplotlib.pyplot as plt

n_data = 100
n_class = 4
cmap = plt.colormaps['tab10']
colors = [cmap(i) for i in range(n_class)]

fig, ax = plt.subplots(figsize=(7, 7))
for class_idx in range(n_class):
    centroid = np.random.uniform(-10, 10, (2, 1))
    data = np.random.normal(centroid[class_idx], 1, (n_data, 2))
    ax.scatter(centroid[0], centroid[1],
               s=100,
               c='black')
    ax.scatter(data[:, 0], data[:, 1],
               facecolor='None',
               alpha=0.5,
               c=colors[class_idx])
    print(data.shape)

fig.tight_layout()
plt.show()