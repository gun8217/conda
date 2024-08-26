import numpy as np
import matplotlib.pyplot as plt

n_data = 100
radius = [5, 10]
centers = [np.array([0, 0]), np.array([15, 15])]
colors = ['blue', 'red', 'green', 'orange']


fig, ax = plt.subplots(figsize=(7, 7))

for i in range(len(radius)):
    angles = np.random.uniform(0, 4 * np.pi, n_data)
    radii_values = np.random.uniform(0, radius[i], n_data)
    x = centers[i][0] + radii_values * np.cos(angles)
    y = centers[i][1] + radii_values * np.sin(angles)
    data = np.column_stack((x, y))

    ax.scatter(data[:, 0], data[:, 1],
               color=colors[i])


fig.tight_layout()
plt.show()