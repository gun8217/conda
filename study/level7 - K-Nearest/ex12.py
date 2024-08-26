import numpy as np
import matplotlib.pyplot as plt

n_data_per_class = 100
n_classes = 4
n_features = 2

centroids = np.random.uniform(-10, 10, (n_classes, 2))

X_list = []
y_list = []

for class_idx in range(n_classes):
    data = np.random.normal(centroids[class_idx], 1, (n_data_per_class, n_features))
    X_list.append(data)
    y_list.append(np.full((n_data_per_class,), class_idx))

X = np.vstack(X_list)
y = np.hstack(y_list)
print(y)
fig, ax = plt.subplots(figsize=(8, 8))
colors = ['red', 'blue', 'green', 'purple']

for class_idx in range(n_classes):
    mask = y == class_idx
    ax.scatter(X[mask, 0], X[mask, 1], c=colors[class_idx])

for centroid in centroids:
    ax.scatter(centroid[0], centroid[1], c='black', marker='x', s=100)

plt.show()