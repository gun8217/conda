import numpy as np

P1 = np.array([3/7, 2/7, 2/7])
H1 = -np.sum(P1 * np.log2(P1))
print(H1)

# P1_child = np.array([3/10, 7/10])
# H1_child = -np.sum(P1_child * np.log2(P1_child))

# IG = H1 - ((H1_child * 1/2) + (H1_child * 1/2))

# print(IG)