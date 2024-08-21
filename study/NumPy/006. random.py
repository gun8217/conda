# 표준정규분포 분포도 : 68%, 95%, 99.7%, 이외는 outline이라 함.

import numpy as np

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

normal = np.random.normal(loc=[-2, 0, 3],
                          scale=[1, 2, 5],
                          size=(200, 3))


normal1 = np.random.rand(3, 2)
print(normal1)
print()

normal2 = np.random.uniform(-1, 0, 10)
print(normal2)
print()

normal3 = np.random.randint([1, 3, 5, 7], [[10], [20]], dtype=np.uint8)
print(normal3)