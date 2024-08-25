import numpy as np

# 문제 1: 배열 생성과 기본 연산
# 1부터 20까지의 숫자로 이루어진 1차원 배열을 생성하세요.
datas = np.arange(1, 21)
# 위에서 생성한 배열에서 짝수만 선택하세요.
even = datas[datas % 2 == 0]
# 배열의 모든 요소에 3을 곱하세요.
mul_datas = datas * 3
# 배열의 모든 요소의 합과 평균을 계산하세요.
add_datas = datas.sum()
mean_datas = datas.mean()

# 문제 2: 배열 인덱싱과 슬라이싱
# 3x3의 2차원 배열을 생성하세요. 배열의 값은 1부터 9까지의 숫자로 하세요.
datas = np.arange(1, 10).reshape(3, -1)
# 2행 3열의 요소를 선택하세요.
select = datas[1, 2]
# 첫 번째 행과 두 번째 열을 추출하여 새로운 배열을 만드세요.
first_row = datas[0, :]
second_column = datas[:, 1]
result = np.vstack((first_row, second_column))
result = np.array([datas[0, :], datas[:, 1]])
# 배열의 대각선 요소를 선택하세요.
diagonal = np.diag(datas)

# 문제 3: 배열의 형태 변경
# 1부터 12까지의 숫자로 이루어진 1차원 배열을 생성한 후, 이를 3x4의 2차원 배열로 변환하세요.
datas = np.arange(1, 13).reshape(3, -1)
# 위 배열을 다시 4x3의 배열로 변환하세요.
reshape_dats = datas.reshape(4, -1)
# 배열을 1차원 배열로 변환하세요.
flatten_datas = reshape_dats.flatten()

# 문제 4: 배열 연산
# 2x3 크기의 배열 A와 B를 각각 랜덤하게 생성하세요.
data_A = np.random.randint(0, 10, (2, 3))
data_B = np.random.randint(0, 10, (2, 3))
# 배열 A와 B의 요소별 덧셈, 뺄셈, 곱셈, 나눗셈을 수행하세요.
add_ = np.add(data_A, data_B)
subt_ = np.subtract(data_A, data_B)
mul_ = np.multiply(data_A, data_B)
div_ = np.divide(data_A, data_B, where=data_B!=0)
# 배열 A의 모든 요소의 제곱근을 구하세요.
squard_ = np.sqrt(data_A)
# 배열 A와 B의 행렬 곱을 계산하세요.
data_B_ = data_B.T
matmul1 = np.matmul(data_A, data_B_)
matmul2 = data_A @ data_B_

# 문제 5: 조건을 이용한 배열 처리
# 1부터 20까지의 숫자로 이루어진 1차원 배열을 생성하세요.
datas = np.arange(1, 21)
# 배열에서 5의 배수만 선택하세요.
result = datas[datas % 5 == 0]
# 배열의 요소 중 10보다 큰 숫자는 1로, 그렇지 않은 숫자는 0으로 바꾸세요.
new_datas = np.where(datas > 10, 1, 0)
# 배열에서 짝수인 숫자를 모두 음수로 바꾸세요.
data_ = np.where(datas % 2 == 0, -datas, datas)

# 문제 6: numpy의 통계 함수 활용
# 10x10 크기의 랜덤 배열을 생성하세요.
datas = np.random.randint(0, 100, (10, 10))
# 배열의 전체 평균, 행별 평균, 열별 평균을 계산하세요.
mean_all = np.mean(datas)
mean_axis0 = np.mean(datas, axis=0)
mean_axis1 = np.mean(datas, axis=1)
# 배열의 최댓값과 최솟값을 찾으세요.
max_v = np.max(datas)
min_v = np.min(datas)
# 배열에서 최댓값이 있는 위치(인덱스)를 찾으세요.
max_index = np.unravel_index(np.argmax(datas), datas.shape)