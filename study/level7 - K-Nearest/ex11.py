import numpy as np
import matplotlib.pyplot as plt

n_data = 100
n_classes = 4

centroid = np.random.uniform(-10, 10, (n_classes, 2))

X_list, y_list = [], []
for class_idx in range(n_classes):
    data = np.random.normal(centroid[class_idx], 1, (n_data, 2))

    X_list.append(data)
    y_list.append(np.full((n_data,), class_idx))

X = np.vstack(X_list)
y = np.hstack(y_list)
print(X.shape, y.shape)