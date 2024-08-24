import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot()

ax.grid()
ax.tick_params(axis='both',
               labelsize=15)

ax.text(x=0.6, y=0.4,
        s="Hello",
        fontsize=15,
        va='center', ha='left')

plt.show()