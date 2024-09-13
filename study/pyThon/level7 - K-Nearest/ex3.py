import numpy as np
import matplotlib.pyplot as plt

K = 4
n_classes = 4
n_data = 50

X, y = [], []
for class_idx in range(n_classes):
    centroid = np.random.uniform(low=-10, high=10, size=(2,))
    X_ = np.random.normal(loc=centroid, scale=1.7, size=(n_data, 2))
    y_ = np.ones(n_data,) * class_idx
    X.append(X_); y.append(y_)
X = np.vstack(X)
y = np.concatenate(y)

test_data = np.random.uniform(low=-10, high=10, size=(2,))

e_dists = np.sqrt(np.sum((X - test_data)**2, axis=1))

select_dist = np.argsort(e_dists)[:K]
data_xs = X[select_dist]; data_y = y[select_dist]
print(data_y)
uniques, cnts = np.unique(data_y, return_counts=True)
print(uniques, cnts)
pred = int(uniques[np.argmax(cnts)])
print(f"test data is classified as class number {pred}")

fig, ax = plt.subplots(figsize=(8, 8))
for class_idx in range(n_classes):
    X_ = X[y == class_idx]
    ax.scatter(X_[:, 0], X_[:, 1], alpha=0.5)
    ax.scatter(test_data[0], test_data[1], color=f'C{pred}', s=200, marker="*")

k_nearest_data = X[select_dist]
k_nearest_y = y[select_dist]
for data, y_ in zip(k_nearest_data, k_nearest_y):
   ax.plot([test_data[0], data[0]], [test_data[1], data[1]], ls=':', lw=2,
           color=f'C{int(y_)}')
   ax.text(test_data[0]+0.5, test_data[1], f"class {pred}", color='fuchsia', fontsize=20)

x1_lim, x2_lim = ax.get_xlim(), ax.get_ylim()
x1 = np.linspace(x1_lim[0], x1_lim[1], 100)
x2 = np.linspace(x2_lim[0], x2_lim[1], 100)
X1, X2 = np.meshgrid(x1, x2)
X_db = np.hstack([X1.reshape(-1, 1), X2.reshape(-1, 1)])

preds = []
for x_db in X_db:
    distances = np.sum((X - x_db) ** 2, axis=1)
    distances_argsort = np.argsort(distances)
    close_K_indices = distances_argsort[:K]
    close_classes = y[close_K_indices]
    unique, cnts = np.unique(close_classes, return_counts=True)
    pred = unique[np.argmax(cnts)]
    preds.append(pred)
preds = np.array(preds)
preds = np.array(preds)
print(len(preds))

for class_idx in range(n_classes):
    X_ = X_db[preds == class_idx]
    ax.scatter(X_[:, 0], X_[:, 1], color=f'C{class_idx}', alpha=0.1)

fig.tight_layout()
plt.show()