import numpy as np
import matplotlib.pyplot as plt

n_class = 4
n_data = 100
K = 9
cmap = plt.colormaps['tab10']
colors = [cmap(i) for i in range(n_class)]

centroids = np.random.uniform(low=-10, high=10, size=(n_class, 2))
test_data = np.random.uniform(low=-10, high=10, size=(n_class, 2))

X_list = []; y_list = []; test_list = []
for i in range(n_class):
    X_ = np.random.normal(loc=centroids[i], scale=1, size=(n_data, 2))
    test_ = np.random.normal(loc=test_data[i], scale=1, size=(n_data, 2))
    X_list.append(X_)
    y_list.append(np.full(n_data, i))
    test_list.append(test_)

X = np.vstack(X_list)
y = np.hstack(y_list)
test = np.vstack(test_list)

euc_dist = np.sum(((X - test)**2), axis=1)**0.5

argsort = np.argsort(euc_dist)
select_dist = argsort[:K]
class_ = y[select_dist]
class_xs = X[select_dist]
print(class_xs)
class_m = np.unique(class_, return_counts=True)
argmax_idx = np.argmax(class_m[1])
idx_value = class_m[0][argmax_idx]

fig, ax = plt.subplots(figsize=(7, 7))
for i in range(n_class):
    ax.scatter(X[y == i][:, 0], X[y == i][:, 1],
               color=colors[i], alpha=0.4, s=75)

# ax.scatter(centroids[:, 0], centroids[:, 1],
#            color='black', marker='x', linewidth=2, s=100)

test_point = test_data[idx_value]

ax.scatter(test_point[0], test_point[1],
           color='gray', marker='*', linewidth=2, s=150)

ax.annotate(f'Class {idx_value}', (test_point[0], test_point[1]),
            textcoords="offset points", xytext=(0,10), ha='center', fontsize=12)
ax.plot(class_xs[0], class_xs[1])

fig.tight_layout()
plt.show()