import numpy as np

d12 = np.array([5.00, 2.50])
d5 = np.array([2.75, 7.50])
d17 = np.array([5.25, 9.50])


def func_eucDist(u, v):
    euc_dist = np.sum((u - v)**2)**0.5
    return euc_dist


def func_manhDist(u, v):
    manh_dist = np.sum(np.abs(u - v))
    return manh_dist


print(f"{func_eucDist(d12, d5) = }")
print(f"{func_eucDist(d12, d17) = }\n")

print(f"{func_manhDist(d12, d5) = }")
print(f"{func_manhDist(d12, d17) = }")