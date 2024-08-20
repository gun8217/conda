# 표준정규분포 분포도 : 68%, 95%, 99.7%, 이외는 outline이라 함.

import numpy as np

normal1 = np.random.rand(3, 2)
print(normal1)
print()
normal2 = np.random.uniform(-1, 0, 10)
print(normal2)
print()
normal3 = np.random.randint([1, 3, 5, 7], [[10], [20]], dtype=np.uint8)
print(normal3)