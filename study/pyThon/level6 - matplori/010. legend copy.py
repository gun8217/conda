import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 100)
sin_data = np.sin(t)
cos_data = np.cos(t)

fig, ax = plt.subplots()

# ax.plot(t, sin_data, label='sin(t)', color='blue')
# ax.plot(t, cos_data, label='cos(t)', color='red')

for ax_idx in range(12):
    label_temp = 'added by {}'
    ax.plot(t, sin_data + ax_idx,
            label=label_temp.format(ax_idx))

ax.legend(fontsize=9, loc='upper right', ncol=3)

ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.set_title('Sin & Cos')
ax.grid(alpha=0.75)

plt.show()