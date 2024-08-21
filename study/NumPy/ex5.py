import numpy as np

# np.arange : 범위 내 연속된 숫자
a = np.arange(10)
b = np.arange(12).reshape((3, 4))

# np.linspace 범위 내 균등 분포
a = np.linspace(0, 10, 5)
b = np.linspace(0, 10, 12).reshape((3, 4))

# np.ones : 1 값으로 채워진 배열
a = np.ones(5)
b = np.ones((3, 4))

# np.ones : 0 값으로 채워진 배열
a = np.zeros(5)
b = np.zeros((3, 4))

# np.full은 지정된 값으로 채워진 배열(inf - 무한대)
a = np.full(5, 7)
b = np.full((2, 3), 7)

# np.random.rand: 0과 1 사이 균등 분포
a = np.random.rand(5)
b = np.random.rand(3, 4)

# np.random.randint: 정수
a = np.random.randint(0, 10, size=5)
b = np.random.randint(0, 10, size=(3, 4))

# np.random.normal: 정규 분포
a = np.random.normal(loc=0.0, scale=1.0, size=5)
b = np.random.normal(loc=0.0, scale=1.0, size=(3, 4))

# np.eye : 단위 행렬
a = np.eye(3)