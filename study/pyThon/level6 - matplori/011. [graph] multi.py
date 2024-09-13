import matplotlib.pyplot as plt
import numpy as np

PI = np.pi
t = np.linspace(-4*PI, 4*PI, 300)
sin = np.sin(t)

fig, ax = plt.subplots(figsize=(5, 5))

for ax_idx in range(12):
    label_template = 'added by {}'
    ax.plot(t, sin + ax_idx,
             label=label_template.format(ax_idx))

ax.legend(bbox_to_anchor=(1, 0.5), loc='center left')

fig.tight_layout()
plt.show()