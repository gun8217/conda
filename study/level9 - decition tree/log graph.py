import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 10, 400)

log_x = np.log2(x)
neg_log_x = -log_x

plt.figure(figsize=(10, 5))

plt.plot(x, log_x, color='blue')
plt.plot(x, neg_log_x, color='red', linestyle='--')

plt.show()