import numpy as np

M = np.random.randint(1, 5, (2, 3))
N = np.random.randint(1, 5, (2, 3))

print("M:", M)
print("N:", N, '\n')

print("M + N:", M + N)
print("M - N:", M - N)

print("M > N:", M > N)
print("M >= N:", M >= N)