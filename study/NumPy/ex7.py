# 표준정규분포 분포도 : 68%, 95%, 99.7%, 이외는 outline이라 함.

import numpy as np

normal = np.random.normal(loc=[-2, 0, 3],
                          scale=[1, 2, 5],
                          size=(200, 3))