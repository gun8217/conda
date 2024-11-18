from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

n_samples = 300

X, y = make_moons(n_samples=n_samples, noise=0.15)

fig, ax = plt.subplots(figsize=(10, 10))

X_pos, X_neg = X[y == 1], X[y == 0]
ax.scatter(X_pos[:, 0], X_pos[:, 1], color='blue')
ax.scatter(X_neg[:, 0], X_neg[:, 1], color='red')
ax.tick_params(labelsize=15)

plt.show()