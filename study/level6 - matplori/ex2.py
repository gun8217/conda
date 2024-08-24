import numpy as np
import matplotlib.pyplot as plt

n_class = 5

data = np.vstack([np.random.rand(30, 2) + i for i in range(n_class)])
labels = np.array([f'class{i}' for i in range(n_class) for _ in range(30)])

noise = np.random.normal(0, 0.1, data.shape)
noise_data = data + noise

colors = ['blue', 'green', 'red', 'purple', 'orange']

fig, ax = plt.subplots(figsize=(8, 6))

for i in range(n_class):
    class_data = noise_data[labels == f'class{i}']
    plt.scatter(class_data[:, 0], class_data[:, 1],
                color=colors[i],
                marker='o',
                alpha=0.7,
                facecolor='None',
                label=f'class{i}')

ax.set_xticks([-10, -5, 0, 5, 10, 15, 20])
ax.set_yticks([-10, -5, 0, 5, 10, 15, 20])
ax.grid(alpha=0.75)
ax.legend(loc='center left',
          bbox_to_anchor=(1.05, 0.5))

fig.subplots_adjust(left=0.2, right=0.8, bottom=0.2, top=0.8)
plt.show()