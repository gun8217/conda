import numpy as np

a= np.arange(27).reshape((3, 3, -1))

# print(a[0])
# print(a[1])
# print(a[2])

# print(a[0][0], a[0][1], a[0][2], a[0][3])
# print(a[1][0], a[1][1], a[1][2], a[1][3])
# print(a[2][0], a[2][1], a[2][2], a[2][3])

# print(a[0, 0], a[0, 1], a[0, 2], a[0, 3])
# print(a[1, 0], a[1, 1], a[1, 2], a[1, 3])
# print(a[2, 0], a[2, 1], a[2, 2], a[2, 3])

# print(a[0, 1:])
# print(a[1, :-1])
# print(a[2, 1:-1])

# print(a[:, :-1, :])
# print(a[:, :, 0])
print(a[1:, -2:, -2:])