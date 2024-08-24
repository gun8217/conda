import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 5))

random_values = np.random.randn(300)
ax.hist(random_values, bins=50)
plt.show()
print(random_values.shape)