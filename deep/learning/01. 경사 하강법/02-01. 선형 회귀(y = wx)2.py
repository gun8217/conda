import numpy as np
import matplotlib.pyplot as plt

n_data = 100
w_t = 2

rng = np.random.default_rng(0)
x = rng.normal(0, 1, n_data)
noise = rng.normal(0, 1, n_data)
y = w_t * x + 0.1 * noise # y = wx + noise

fig, ax = plt.subplots(dpi=200)
ax.scatter(x, y, alpha=0.5)

w = -1
x_model = np.array(ax.get_xlim())
y_model = x_model * w
cmap = plt.colormaps['rainbow']
colors = cmap(np.linspace(0, 1, len(x)))
ax.plot(x_model, y_model, color=colors[0], lw=3)

fig.tight_layout()
plt.show()