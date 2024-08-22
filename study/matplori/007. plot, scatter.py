import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n_data = 100
x_data = np.random.normal(0, 1, (n_data,))
y_data = np.random.normal(0, 1, (n_data,))

fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(x_data, y_data, s=1, color='r')
# ax.plot(x_data, y_data, 'o')

plt.show()