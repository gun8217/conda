import numpy as np

# 기초 문제 - 텐서 생성
# 1차원 텐서(벡터) [1, 2, 3, 4, 5]를 생성하세요.
tensor_vec = np.arange(1, 6)
# 2차원 텐서(행렬) [[1, 2, 3], [4, 5, 6]]를 생성하세요.
tensor_mat = np.arange(1, 7).reshape(2, 3)
# 3차원 텐서의 차원이 각각 (2, 3, 4)인 텐서를 생성하세요.
tensor_multi = np.arange(1, 25).reshape(2, 3, -1)

# 텐서 연산
# 두 텐서 A = [1, 2, 3]와 B = [4, 5, 6]을 더하세요.
tensor_A = np.arange(1, 4)
tensor_B = np.arange(4, 7)
tensor_add = np.add(tensor_A, tensor_B)
# 텐서 C = [[1, 2], [3, 4]]의 각 원소에 10을 더하세요.
tensor_C = np.arange(1, 5).reshape(2, -1)
tensor_add2 = np.add(tensor_C, 10)
# 텐서 D = [[1, 2], [3, 4]]의 전치(transpose)를 구하세요.
tensor_D = np.arange(1, 5).reshape(2, -1)
tensor_trans = tensor_D.T

# 중급 문제 - 텐서 슬라이싱
# 텐서 E = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]에서 두 번째 행만 추출하세요.
tensor_E = np.arange(1, 10).reshape(3, -1)
slice1 = tensor_E[1, :]
# 텐서 F = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]에서 첫 번째 차원에서 두 번째 텐서만 추출하세요.
tensor_F = np.arange(1, 9).reshape(2, 2, -1)
# slice2 = tensor_F[0, 1, :]
slice2 = tensor_F[1, :, :]
print(slice2)

# 텐서 결합
# 두 텐서 G = [[1, 2]]와 H = [[3, 4]]을 수직으로 결합하세요.
tensor_G = np.arange(1, 3).reshape(1, -1)
tensor_H = np.arange(3, 5).reshape(1, -1)
v_stack = np.vstack([tensor_G, tensor_H])
# 두 텐서 I = [[1, 2], [3, 4]]와 J = [[5, 6], [7, 8]]을 수평으로 결합하세요.
tensor_I = np.arange(1, 5).reshape(2, -1)
tensor_J = np.arange(5, 9).reshape(2, -1)
h_stack = np.hstack([tensor_I, tensor_J])

# 고급 문제 - 텐서 연산
# 텐서 K와 L이 주어졌을 때, 두 텐서의 행렬 곱셈을 수행하세요. 텐서 K는 [[1, 2], [3, 4]], 텐서 L은 [[5, 6], [7, 8]]입니다.
tensor_K = np.arange(1, 5).reshape(2, -1)
tensor_L = np.arange(5, 9).reshape(2, -1)
matmul = tensor_K @ tensor_L
# 텐서 M = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]의 모든 원소에 대해 평균값을 계산하세요.
tensor_M = np.arange(1, 9).reshape(2, 2, -1)
tensor_mean = np.mean(tensor_M)

# 텐서 변형
# 텐서 N = [1, 2, 3, 4, 5, 6]을 (2, 3) 형태로 변형하세요.
tensor_N = np.arange(1, 7).reshape(2, -1)
# 텐서 O를 2D 형태로 변형한 후, 각 열의 합계를 구하세요. 텐서 O는 [[1, 2, 3], [4, 5, 6], [7, 8, 9]]입니다.
tensor_O = np.arange(1, 10).reshape(3, -1)
y_sum = np.sum(tensor_O, axis=0)