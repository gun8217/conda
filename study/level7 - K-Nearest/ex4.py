import numpy as np
import matplotlib.pyplot as plt

center = np.random.uniform(-5, 5, (2,))

n_data = 100
data = np.random.normal(loc=center, scale=1, size=(n_data, 2))

fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(center[0], center[1], c='red')
ax.scatter(data[:, 0], data[:, 1])

fig.tight_layout()
plt.show()