import numpy as np
import matplotlib.pyplot as plt

n_class = 4
n_data = 100
K = 5
cmap = plt.colormaps['tab10']
colors = [cmap(i) for i in range(n_class)]

centroids = np.random.uniform(low=-10, high=10, size=(n_data, 2))
test_data = np.random.uniform(low=-10, high=10, size=(2,))

X_list = []; y_list = []
for i in range(n_class):    
    X_ = np.random.normal(loc=centroids[i], scale=1, size=(n_data, 2))
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

fig, ax = plt.subplots(figsize=(10, 10))
for i in range(n_class):
    ax.scatter(X[y == i][:, 0], X[y == i][:, 1],
               color=colors[i], alpha=0.4, s=75)

text = ax.annotate(f'Class {idx_value}', (test_data[0], test_data[1]),
            textcoords="offset points", xytext=(0, 10), ha='center', va='bottom',
            fontsize=24)
text.set_alpha(.4)
ax.scatter(test_data[0], test_data[1],
           color='black', marker='*', linewidth=2, s=150)

for i in range(K):
    ax.plot([test_data[0], class_xs[i][0]],
            [test_data[1], class_xs[i][1]],
            color='gray', linestyle='--')

x1_lim, x2_lim = ax.get_xlim(), ax.get_ylim()
x1 = np.linspace(x1_lim[0], x1_lim[1], 100)
x2 = np.linspace(x2_lim[0], x2_lim[1], 100)
X1, X2 = np.meshgrid(x1, x2)
X_db = np.hstack([X1.reshape(-1, 1), X2.reshape(-1, 1)])

preds = []
for x_db in X_db:
    dist = np.sum((X - x_db)**2, axis=1)
    dist_sort = np.argsort(dist)
    near_idx = dist_sort[:K]
    near_class = y[near_idx]
    unique, count = np.unique(near_class, return_counts=True)
    pred = unique[np.argmax(count)]
    preds.append(pred)
preds = np.array(preds)
print(len(preds))

for idx in range(n_class):
    X_ = X_db[preds == idx]
    ax.scatter(X_[:, 0], X_[:, 1], color=f'C{idx}', alpha=0.1)

fig.tight_layout()
plt.show()