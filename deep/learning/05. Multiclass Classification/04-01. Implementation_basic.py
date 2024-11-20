# 데이터는 2개의 feature와 4개의 클래스를 가지도록 만듦

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

n_samples = 100
n_classes = 4

X, y = make_blobs(n_samples=n_samples, centers=n_classes,
                  n_features=2, cluster_std=0.7, random_state=1)

fig, ax = plt.subplots(figsize=(10, 10))

for class_idx in range(n_classes):
    class_X = X[y == class_idx]
    ax.scatter(class_X[:, 0], class_X[:, 1])

ax.tick_params(labelsize=15)

plt.show()