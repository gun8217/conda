import numpy as np
import matplotlib.pyplot as plt

n_class = 5

data_ranges = [
    [(-10, 5), (10, 20)],
    [(-10, 5), (0, 10)],
    [(-2, 2), (2, 10)],
    [(0, 10), (-2, 7)],
    [(10, 20), (-10, 0)]
]
data = np.vstack([np.random.rand(30, 2) + i for i in range(n_class)])

data = []
for i in range(n_class):
    x_min, x_max = data_ranges[i][0]
    y_min, y_max = data_ranges[i][1]
    x_data = np.random.uniform(x_min, x_max, 30)
    y_data = np.random.uniform(y_min, y_max, 30)
    class_data = np.stack((x_data, y_data), axis=-1)
    data.append(class_data)

data = np.vstack(data)
labels = np.array([f'class{i}' for i in range(n_class) for _ in range(30)])

noise = np.random.normal(0, 0.1, data.shape)
noise_data = data + noise

colors = ['red', 'green', 'blue', 'orange', 'purple']

fig, ax = plt.subplots(figsize=(8, 6))

for i in range(n_class):
    class_data = noise_data[labels == f'class{i}']
    ax.scatter(class_data[:, 0], class_data[:, 1],
                color=colors[i],
                marker='o',
                s=50,
                linewidth=2.5,
                alpha=0.4,
                facecolor='None',
                label=f'class{i}')

ax.set_xticks([-5, 0, 5, 10, 15, 20, 25])
ax.set_yticks([-5, 0, 5, 10, 15, 20])
ax.legend(loc='center left',
          bbox_to_anchor=(1, 0.5))

fig.subplots_adjust(left=0.1, right=0.82, bottom=0.1, top=0.95)
plt.show()