import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n_class = 5
n_data = 30

center_pt = np.random.uniform(-20, 20, (n_class, 2))
cmap = plt.colormaps['tab10']
colors = [cmap(i) for i in range(n_class)]

data = []
for class_idx in range(n_class):
    center = center_pt[class_idx]
    class_data = center + 2 * np.random.normal(0, 1, (n_data, 2))
    data.append(class_data)
data = np.vstack(data)

fig, ax = plt.subplots(figsize=(6, 5))
for class_idx in range(n_class):
    ax.scatter(data[class_idx * n_data: (class_idx + 1) * n_data, 0],
                data[class_idx * n_data: (class_idx + 1) * n_data, 1],
                s=100,
                facecolor='None',
                edgecolor=colors[class_idx],
                linewidth=5,
                alpha=0.5,
                label='class' + str(class_idx))
ax.legend(loc='center left',
            bbox_to_anchor=(1, 0.5),
            labelspacing=0.65)

fig.tight_layout()
plt.show()