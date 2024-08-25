import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
t = np.linspace(-4*PI, 4*PI, 1000)
sin, cos, tan = np.sin(t), np.cos(t), np.tan(t)

tan[:-1][np.diff(tan) < 0] = np.nan
data = np.vstack((sin, cos, tan))
title_list = [r'$sin(t)$', r'$cos(t)$', r'$tan(t)$']
x_ticks = np.arange(-4*PI, 4*PI+PI, PI)
x_ticklabels = [str(i) + r'$\pi$' for i in range(-4, 5)]

fig, axes = plt.subplots(3, 1,
                         figsize=(3, 5),
                         sharex=True)

for ax_idx, ax in enumerate(axes.flat):
    ax.plot(t, data[ax_idx])
    ax.set_title(title_list[ax_idx],
                 fontsize=13)
    ax.tick_params(labelsize=10)
    ax.grid()
    if ax_idx == 2:
        ax.set_ylim([-3, 3])

axes[-1].set_xticks(x_ticks)
axes[-1].set_xticklabels(x_ticklabels)


fig.subplots_adjust(left=0.1, right=0.95, bottom=0.05, top=0.95)
plt.show()