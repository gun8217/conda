import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 10)
sin_data = np.sin(t)
cos_data = np.cos(t)

fig, axes = plt.subplots(3, 1, figsize=(6, 9))

axes[0].plot(x, y1, marker='o', linestyle='-', color='b', label='sin(x)')
axes[1].plot(x, y2, marker='D', linestyle='-', color='r', label='cos(x)')
axes[2].plot(x, y3, marker='s', linestyle='-', color='g', label='tan(x)')

for ax in axes:
    a.legend(fontsize=9, ncol=1, loc='center right', bbox_to_anchor=(-0.225, 0.5))

ax[0].set_xlabel('Time')
ax[0].set_ylabel('Value')
ax[0].set_title('Sin & Cos')

for a in ax:
    a.grid(alpha=0.75)

fig.subplots_adjust(left=0.3, right=0.7, bottom=0.3, top=0.7)
plt.show()