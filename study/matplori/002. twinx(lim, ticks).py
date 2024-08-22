import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5, 5))
ax1 = fig.add_subplot()
ax2 = ax1.twinx()

ax1.set_xlim([0, 4])
ax1.set_xticks([0, 1, 5, 10])

ax1.set_ylim([0, 100])
ax2.set_ylim([0, 0.1])
yticks = [i for i in range(4)]
ax2.set_yticks(yticks)


fig.tight_layout()
plt.show()