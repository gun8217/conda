import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 100)
sin_data = np.sin(t)
cos_data = np.cos(t)

fig, ax = plt.subplots()

# ax.plot(t, sin_data, label='sin(t)', color='blue')
# ax.plot(t, cos_data, label='cos(t)', color='red')

for ax_idx in range(3):
    label_temp = 'added by {}'
    ax.plot(t, sin_data + ax_idx,
            label=label_temp.format(ax_idx))

ax.legend(fontsize=9,
          ncol=1,
          loc='center right',
          bbox_to_anchor=(-0.225, 0.5)          
        #   loc='center left',
        #   bbox_to_anchor=(1.05, 0.5)
        #   loc='lower center',
        #   bbox_to_anchor=(0.5, 1.12)          
        #   loc='upper center',
        #   bbox_to_anchor=(0.5, -0.24)
        )

ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.set_title('Sin & Cos')
ax.grid(alpha=0.75)

ax[0].plot(marker='o')
ax[1].plot(marker='D')
ax[2].plot(marker='s')

fig.subplots_adjust(left=0.3, right=0.7, bottom=0.3, top=0.7)
plt.show()