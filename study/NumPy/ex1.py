import numpy as np

M = np.array([1, 2, 3], dtype=float)
print(M)
print(M.dtype)
print()

N = np.array([1, 2, 3], dtype=int)
print(N)
print(N.dtype)
print()

O = M.astype(int)
print(O)
print(O.dtype)
print()

P = N.astype(float)
print(P)
print(P.dtype)

R = np.random.uniform(low=10, high=10, size=(3, 3))
print(R, '\n')
print(R.astype(int))