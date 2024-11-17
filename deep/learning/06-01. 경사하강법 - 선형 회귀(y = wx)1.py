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

fig.tight_layout()
plt.show()