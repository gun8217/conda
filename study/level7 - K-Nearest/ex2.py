import numpy as np
import matplotlib.pyplot as plt

n_class = 4
n_data = 100
K = 5
cmap = plt.colormaps['tab10']
colors = [cmap(i) for i in range(n_class)]

X_list = []; y_list = []
for i in range(n_class):
    centroid = np.random.uniform(low=-10, high=10, size=(2,))
    X_ = np.random.normal(loc=centroid[i], scale=1, size=(n_data, 2))
    X_list.append(X_)
    y_list.append(np.full(n_data, i))

X = np.vstack(X_list)
y = np.hstack(y_list)

euc_dist = np.sqrt(np.sum(((X - test_data)**2), axis=1))
argsort = np.argsort(euc_dist)
select_dist = argsort[:K]
class_ = y[select_dist]; class_xs = X[select_dist]
class_m = np.unique(class_, return_counts=True)
argmax_idx = np.argmax(class_m[1])
idx_value = class_m[0][argmax_idx]

fig, ax = plt.subplots(figsize=(7, 7))
for i in range(n_class):
    ax.scatter(X[y == i][:, 0], X[y == i][:, 1],
               color=colors[i], alpha=0.4, s=75)

ax.scatter(test_data[0], test_data[1],
           color='gray', marker='*', linewidth=2, s=150)
ax.annotate(f'Class {idx_value}', (test_data[0], test_data[1]),
            textcoords="offset points", xytext=(0,10), ha='center', va='bottom', fontsize=12)

for i in range(K):
    ax.plot([test_data[0], class_xs[i][0]],
            [test_data[1], class_xs[i][1]],
            color='gray', linestyle='--')



fig.tight_layout()
plt.show()