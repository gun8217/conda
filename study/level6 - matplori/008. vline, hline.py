import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 7))

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])

ax.axvline(x=1,
           ymax=0.5, ymin=0.2,
           color='black',
           linewidth=1,
           linestyle=':') # .. -. -- -

ax.axhline(y=1,
           xmax=0.5, xmin=0.2,
           color='red',
           linewidth=1,
           linestyle='--')


plt.tight_layout()
plt.show()