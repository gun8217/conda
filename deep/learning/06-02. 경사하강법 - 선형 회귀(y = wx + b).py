import numpy as np
import matplotlib.pyplot as plt

n_data = 20
w_t, b_t = 2, 1

rng = np.random.default_rng(0)
x = rng.normal(0, 1, n_data)
noise = rng.normal(0, 1, n_data)
y = w_t * x + b_t + 0.1 * noise # y = wx + noise

fig, ax = plt.subplots(dpi=200)
ax.scatter(x, y, alpha=0.5)

w, b = -1, -2
x_model = np.array(ax.get_xlim())
y_model = x_model * w + b
cmap = plt.colormaps['rainbow']
colors = cmap(np.linspace(0, 1, len(x)))
ax.plot(x_model, y_model, color=colors[0], lw=3)

lr = 0.1
for data_idx, (x_, y_) in enumerate(zip(x, y)):
    pred = w * x_ + b
    dJ_dw = -2*x_*(y_ - pred)
    dJ_db = -2*(y_ - pred)
    w = w - lr * dJ_dw
    b = b - lr * dJ_db
    y_model = x_model * w + b
    ax.plot(x_model, y_model, color=colors[data_idx], alpha=0.5)

ax.axhline(y=0, color='gray', ls='--', lw=0.5)
ax.axvline(x=0, color='gray', ls='--', lw=0.5)

fig.tight_layout()
plt.show()