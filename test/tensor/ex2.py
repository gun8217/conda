import numpy as np

# 기초 문제 - 텐서 생성
# 1차원 텐서 [-1, 0, 1, 2, 3]을 생성하세요.
tensor_1 = np.arange(-1, 4)
# 2차원 텐서 [[10, 20], [30, 40], [50, 60]]을 생성하세요.
tensor_2 = np.arange(10, 61, 10).reshape(3, 2)
# 3차원 텐서의 차원이 각각 (3, 2, 4)인 텐서를 생성하세요.
tensor_3 = np.arange(24).reshape(3, 2, 4)

# 텐서 연산
# 두 텐서 A = [5, 6, 7]과 B = [1, 2, 3]의 원소별 덧셈을 수행하세요.
tensor_A = np.arange(5, 8)
tensor_B = np.arange(1, 4)
tensor_add = np.add(tensor_A, tensor_B)
# 텐서 C = [[3, 6], [9, 12]]의 각 원소에 5를 곱하세요.
tensor_C = np.arange(3, 13, 3).reshape(2, 2)
tensor_mul = np.multiply(tensor_C, 5)
# 텐서 D = [[7, 8], [9, 10]]의 전치를 구하세요.
tensor_D = np.arange(7, 11).reshape(2, 2)
tensor_trans = tensor_D.T

# 중급 문제 - 텐서 슬라이싱
# 텐서 E = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]에서 첫 번째와 두 번째 행만 추출하세요.
tensor_E = np.arange(1, 13).reshape(3, -1)
slice1 = tensor_E[:2, :]
# 텐서 F = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]에서 두 번째 차원에서 첫 번째 열만 추출하세요.
tensor_F = np.arange(1, 13).reshape(2, 2, -1)
print(tensor_F.shape)

# 텐서 결합
# 두 텐서 G = [[1, 2], [3, 4]]와 H = [[5, 6], [7, 8]]을 수직으로 결합하세요.
# 두 텐서 I = [[1, 2, 3], [4, 5, 6]]과 J = [[7, 8, 9], [10, 11, 12]]을 수평으로 결합하세요.\

# 고급 문제 - 텐서 연산
# 텐서 K와 L이 주어졌을 때, 두 텐서의 행렬 곱셈을 수행하세요. 텐서 K는 [[2, 3], [4, 5]], 텐서 L은 [[1, 2], [3, 4]]입니다.
# 텐서 M = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]의 모든 원소에 대해 표준편차를 계산하세요.

# 텐서 변형
# 텐서 N = [10, 20, 30, 40, 50, 60, 70, 80]을 (4, 2) 형태로 변형하세요.
# 텐서 O = [[1, 3, 5], [2, 4, 6], [7, 8, 9]]의 각 행의 평균을 계산하세요.