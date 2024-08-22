import numpy as np

M = np.arange(27)
N = M.reshape((3, 3, 3))
O = N.flatten()

print(M, '\n')
print(N, '\n')
print(O, '\n')