import numpy as np

# np.arange : 범위 내 연속된 숫자
arange1 = np.arange(10)
arange2 = np.arange(12).reshape((3, 4))
print(f"{arange1 = }\n{arange2 = }\n")
# np.linspace 범위 내 균등 분포
linspace1 = np.linspace(0, 10, 5)
linspace2 = np.linspace(0, 10, 12).reshape((3, 4))
print(f"{linspace1 = }\n{linspace2 = }\n")
# np.ones : 1 값으로 채워진 배열
ones1 = np.ones(5)
ones2 = np.ones((3, 4))
print(f"{ones1 = }\n{ones2 = }\n")
# np.ones : 0 값으로 채워진 배열
zeros1 = np.zeros(5)
zeros2 = np.zeros((3, 4))
print(f"{zeros1 = }\n{zeros2 = }\n")
# np.full은 지정된 값으로 채워진 배열(inf - 무한대)
full1 = np.full(5, 7)
full2 = np.full((2, 3), 7)
print(f"{full1 = }\n{full2 = }\n")
# np.eye : 단위 행렬
eye1 = np.eye(3)
print(f"{eye1 = }")

# np.random.rand: 0과 1 사이 균등 분포
random_rand1 = np.random.rand(5)
random_rand2 = np.random.rand(3, 4)
print(f"{random_rand1 = }\n{random_rand2 = }\n")
# np.random.randint: 정수
random_randint1 = np.random.randint(0, 10, size=5)
random_randint2 = np.random.randint(0, 10, size=(3, 4))
print(f"{random_randint1 = }\n{random_randint2 = }\n")
# np.random.normal: 정규 분포
random_normal1 = np.random.normal(loc=0.0, scale=1.0, size=5)
random_normal2 = np.random.normal(loc=0.0, scale=1.0, size=(3, 4))
print(f"{random_normal1 = }\n{random_normal2 = }\n")