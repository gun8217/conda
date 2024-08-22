import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

x_min, x_max = -5, 5
n_data = 300

x_data = np.random.uniform(x_min, x_max, n_data)
# 실제 데이터와 가까운 데이터 구성을 위해 노이즈를 줌
y_data = x_data + 0.5*np.random.normal(0, 1, n_data)

pred_x = np.linspace(x_min, x_max, 2)
pred_y = pred_x

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(x_data, y_data)
ax.plot(pred_x, pred_y, color='r', linewidth=3)

plt.show()