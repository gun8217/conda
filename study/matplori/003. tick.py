import matplotlib.pyplot as plt

fig = plt.figure(figsize=(14, 7))
ax = fig.add_subplot()

ax.tick_params(labelsize=20, length=10, width=3,
               bottom=False, labelbottom=False,
               top=True, labeltop=True,
               left=False, labelleft=False,
               right=True, labelright=True,
               rotation=30)

ax.tick_params(axis='x', rotation=15)
ax.tick_params(axis='y', rotation=0)

plt.show()