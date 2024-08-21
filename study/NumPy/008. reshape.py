import numpy as np

# a = np.arange(12)

# b = a.reshape((2, -1))
# c = a.reshape((3, -1))
# d = a.reshape((4, -1))
# e = a.reshape((6, -1))

# print(a.shape, b.shape, c.shape, d.shape, e.shape)


ab = np.random.randint(0, 10, size=(2, 2))
print(ab)

row_vector = ab.reshape(1, -1) # row - 가로
col_vector = ab.reshape(-1, 1) # col - 세로

print(row_vector.shape, col_vector.shape)