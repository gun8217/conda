import numpy as np
import matplotlib.pyplot as plt

PI = np.pi
t = np.linspace(-4*PI, 4*PI, 300)

sin = np.sin(t)

fig, ax = plt.subplots(figsize=(6, 5))

ax.plot(t, sin, marker='v')
ax.set_title(r'$sin(t)$', fontsize=15)
ax.grid(alpha=0.3)

x_ticks = np.arange(-4*PI, 4*PI+0.1, PI)
x_ticklabels = [str(i) + r'$\pi$'
                for i in range(-4, 5)]
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_ticklabels)

ax.axhline(y=1, color='red', alpha=0.3, linestyle=':')
ax.axhline(y=-1, color='red', alpha=0.3, linestyle=':')

plt.tight_layout()
plt.show()