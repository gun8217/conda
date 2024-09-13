import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
t = np.linspace(-4*PI, 4*PI, 300)
sin = np.sin(t)
cos = np.cos(t)
tan = np.tan(t)

fig, axes = plt.subplots(3, 1,
                         figsize=(7, 10))

axes[0].plot(t, sin)
axes[1].plot(t, cos)
axes[2].plot(t, tan)

y = [1, 2, 3]
y[:-1][np.diff(y) < 0] = np.nan


fig.tight_layout()
plt.show()