import matplotlib.pyplot as plt

# fig = plt.figure(figsize=(7, 7),
#                  facecolor='linen')

# ax = fig.add_subplot()

# # line type
# # ax.plot([2, 3, 1])

# # dot type
# ax.scatter([2, 3, 1], [2, 3, 4])


figsize = (7, 7)
fig, ax = plt.subplots(figsize=figsize)
fig.suptitle("Title of a Figure",
             fontsize=30)
ax.set_title("Title of a Ax",
             fontsize=15)
ax.set_xlabel("X Label",
             fontsize=15,
             color='darkblue',
             alpha=0.7)
ax.set_ylabel("Y Label",
             fontsize=15,
             color='darkblue',
             alpha=0.7)

print(dir(ax))

# 잘린 그래프 여백 맞추기
fig.tight_layout()


plt.show()