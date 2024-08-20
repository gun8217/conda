import numpy as np

# M = np.zeros(shape=(2, 3))
# print(M.shape)
# print(M)

# N = np.ones(shape=(3,), dtype=int)
# print(N.shape)
# print(N)

# F = np.full((3, 2), np.inf)
# print(F.shape)
# print(F)

# M = np.arange(1.5, 10.5)
# print(M.shape)
# print(M)

# M = np.linspace(2.0, 3.0, num=5, endpoint=False)
# print(M)

# 표준편차
# R = np.random.randn()
# print(R)

# randn1 = np.random.randn(3, 5)
# print(randn1)

# 표준정규분포
# R2 = np.random.normal()
# print(R2)

mu, sigma = -2, 1
normal = np.random.normal(mu, sigma, size=(2, 4))
print(normal)
