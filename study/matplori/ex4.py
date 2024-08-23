import numpy as np
import matplotlib.pyplot as plt

n_class = 5
points = 30

centers = np.random.uniform(-5, 20, (n_class, 2))

data = []
labels = []
dataset = {}

for i in range(n_class):
    center = centers[i]
    x_data = np.random.normal(center[0], 1, points)
    y_data = np.random.normal(center[1], 1, points)
    
    class_data = np.stack((x_data, y_data), axis=-1)
    dataset[f'class{i}'] = class_data

data = np.vstack(list(dataset.values()))
labels = np.concatenate([[key] * points for key in dataset.keys()])

noise = np.random.normal(0, 1.75, data.shape)
noise_data = data + noise
colors = ['red', 'green', 'blue', 'orange', 'purple']

fig, ax = plt.subplots(figsize=(8, 6))

for i, class_name in enumerate(dataset.keys()):
    class_data = noise_data[labels == class_name]
    ax.scatter(class_data[:, 0], class_data[:, 1],
                color=colors[i],
                marker='o',
                s=50,
                linewidth=2.5,
                alpha=0.4,
                facecolor='None',
                label=class_name)

ax.set_xticks([-5, 0, 5, 10, 15, 20, 25])
ax.set_yticks([-5, 0, 5, 10, 15, 20])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

fig.subplots_adjust(left=0.1, right=0.82, bottom=0.1, top=0.95)
plt.show()