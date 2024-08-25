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


bools = np.array([True, False])
print(f"bool: \n{bools}")

bools2ints = bools.astype(int)
print(f"int: \n{bools2ints}")

bools2float = bools.astype(float)
print(f"float: \n{bools2float}")


ints = np.array([-2, -1, 0, 1, 2])
floats = np.array([-2.5, -1.5, 0, 1.5, 2.5])

print(f"ints: \n{ints}")
print(f"floats: \n{floats}")

ints2bools = ints.astype(bool)
print(f"bool: \n{ints2bools}")

float2bools = floats.astype(bool)
print(f"float: \n{float2bools}")


strings = np.array(['0', '1', '2', '3'])
print(f"strings: {strings}")

strings2ints = strings.astype(int)
print(f"strings → ints: {strings2ints}")

strings2floats = strings.astype(float)
print(f"strings → floats: {strings2floats}")

strings2bools = strings.astype(bool)
print(f"strings → bools: {strings2bools}")