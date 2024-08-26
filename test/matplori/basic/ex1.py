import numpy as np
import matplotlib.pyplot as plt

# 문제 1: 벡터와 행렬 생성
# 1차원 배열(벡터) [10, 20, 30, 40, 50]을 생성하세요.
vector = np.arange(10, 51, 10)
# 2차원 배열(행렬) [[1, 2], [3, 4], [5, 6]]을 생성하세요.
matr = np.arange(1, 7).reshape(3, 2)

# 문제 2: 배열 연산
# 두 벡터 A = [1, 2, 3]과 B = [4, 5, 6]을 더하여 새로운 벡터를 생성하세요.
vec_A = np.arange(1, 4)
vec_B = np.arange(4, 7)
new_vec = vec_A + vec_B
# 벡터 C = [10, 20, 30]의 각 원소에 5를 더한 벡터를 생성하세요.
vec_C = np.arange(10, 31, 10)
add_vec = vec_C + 5
# 행렬 D = [[1, 2], [3, 4]]의 전치를 구하세요.
matr_D = np.arange(1, 5).reshape(2, 2)
trnas = matr_D.T

# 문제 3: 배열 슬라이싱
# 2차원 배열 E = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]에서 두 번째 행을 추출하세요.
matr_E = np.arange(1, 10).reshape(3, 3)
slice1 = matr_E[1, :]
# 3차원 배열 F = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]에서 첫 번째 차원에서 두 번째 배열을 추출하세요.
matr_F = np.arange(1, 9).reshape(2, 2, 2)
slice2 = matr_F[1, :, :]

# 문제 4: 배열 결합
# 두 배열 G = [1, 2]와 H = [3, 4]을 수직으로 결합하여 새로운 배열을 생성하세요.
matr_G = np.arange(1, 3)
matr_H = np.arange(3, 5)
v_stack = np.vstack([matr_G, matr_H])
# 두 배열 I = [[1, 2], [3, 4]]과 J = [[5, 6], [7, 8]]을 수평으로 결합하여 새로운 배열을 생성하세요.
matr_I = np.arange(1, 5).reshape(2, 2)
matr_J = np.arange(5, 9).reshape(2, 2)
h_stack = np.hstack([matr_I, matr_J])

# 문제 5: 배열 변형 및 시각화
# 1차원 배열 K = [1, 2, 3, 4, 5, 6]을 (2, 3) 형태로 변형하세요.
K = [1, 2, 3, 4, 5, 6]
reshape_K = np.array(K).reshape(2, 3)
# 2차원 배열 L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]의 각 열의 합계를 계산하세요.
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_axis0 = np.sum(L, axis=0)
print(sum_axis0)

# 문제 6: 데이터 생성 및 시각화
# n_data = 50, n_class = 3인 데이터셋을 생성하세요. 각 클래스는 [[1, 1], [5, 5], [10, 10]]을 중심으로 하고, 노이즈를 추가하여 데이터 포인트를 생성하세요.
n_data = 50
n_class = 3
classes = [[1, 1], [5, 5], [10, 10]]

data = []
for idx in range(n_class):
    data_ = np.random.normal(loc=classes[idx], scale=1, size=(n_data, 2))
    data.append(data_)
    print(data_)
    
# data = data.hstack(data)


# 생성한 데이터셋을 산점도로 시각화하고, 각 클래스 중심점을 별도로 표시하세요.
# 각 문제 해결을 위한 가이드
# 문제 1: 벡터와 행렬 생성
# numpy의 np.array 또는 np.arange를 사용하여 배열을 생성합니다.
# 문제 2: 배열 연산
# numpy의 연산 기능 (+, np.add, np.transpose 등)을 사용하여 벡터와 행렬을 연산합니다.
# 문제 3: 배열 슬라이싱
# numpy 배열 인덱싱을 사용하여 특정 행 또는 배열을 추출합니다.
# 문제 4: 배열 결합
# numpy의 np.vstack와 np.hstack을 사용하여 배열을 수직 및 수평으로 결합합니다.
# 문제 5: 배열 변형 및 시각화
# numpy의 reshape과 np.sum을 사용하여 배열을 변형하고 합계를 계산합니다.
# 시각화를 위해 matplotlib를 사용할 수 있습니다.
# 문제 6: 데이터 생성 및 시각화
# numpy를 사용하여 데이터 생성 및 노이즈 추가.
# matplotlib를 사용하여 데이터와 중심점을 시각화합니다.