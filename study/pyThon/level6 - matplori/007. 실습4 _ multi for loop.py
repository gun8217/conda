import numpy as np
import matplotlib.pyplot as plt

PI = np.pi
t = np.linspace(-4*PI, 4*PI, 300)

sin = np.sin(t)
cos = np.cos(t)
tan = np.tan(t)

tan[:-1][np.diff(tan) < 0] = np.nan

data_list = np.vstack((sin, cos, tan))
titles = [r'$sin(t)$', r'$cos(t)$', r'$tan(t)$']

fig, axes = plt.subplots(3, 1,
                         figsize=(6, 5),
                         sharex=True)

for ax, data, title in zip(axes, data_list, titles):
    ax.plot(t, data)
    ax.set_title(title)
    ax.grid()
    if ax == 2:
        ax.set_ylim([-3, 3])

x_ticks = np.arange(-4*PI, 4*PI+0.1, PI)
x_ticklabels = [str(i) + r'$\pi$'
                for i in range(-4, 5)]
axes[2].set_xticks(x_ticks)
axes[2].set_xticklabels(x_ticklabels)
axes[2].set_ylim([-1, 1])
axes[2].set_yticks([-2, 0, 2])

fig.subplots_adjust(left=0.1, right=0.95, bottom=0.05, top=0.95)
# plt.tight_layout()
plt.show()