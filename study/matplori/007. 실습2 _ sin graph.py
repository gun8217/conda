import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
t = np.linspace(-4*PI, 4*PI, 300)
min = np.sin(t)
linear = 0.1*t

fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(t, min)
ax.plot(t, linear)

ax.set_ylim([-1.5, 1.5])

x_ticks = np.arange(-4*PI, 4*PI+0.1, PI)
x_ticklabels = [str(i) + r'$\pi$'
                for i in range(-4, 5)]

ax.set_xticks(x_ticks)
ax.set_xticklabels(x_ticklabels)

ax.tick_params(labelsize=20)
ax.grid()

plt.show()