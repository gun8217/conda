import numpy as np

# 문제 1: 배열의 기본 연산
# 1차원 배열 생성: 1부터 15까지의 숫자로 이루어진 1차원 배열을 생성하세요.
datas = np.arange(1, 16)
# 짝수 배열 선택: 위에서 생성한 배열에서 짝수만 선택하세요.
even = datas[datas % 2 == 0]
# 배열의 제곱: 배열의 모든 요소를 제곱하세요.
squared = np.square(datas)
# 최댓값과 최솟값: 배열의 최댓값과 최솟값을 계산하세요.
max_v = np.max(datas)
min_v = np.min(datas)

# 문제 2: 2차원 배열과 슬라이싱
# 2차원 배열 생성: 1부터 16까지의 숫자로 이루어진 4x4 2차원 배열을 생성하세요.
m_datas = np.arange(1, 17).reshape(4, -1)
# 부분 배열 추출: 위 배열에서 2행 3열부터 4행 4열까지의 부분 배열을 추출하세요.
slice_datas = m_datas[1:4, 2:4]
# 열 평균 계산: 배열의 각 열의 평균을 계산하세요.
mean_axis0 = np.mean(m_datas, axis=0) # 열의 평균은 행의 data를 이용
# 행의 합계 계산: 배열의 각 행의 합계를 계산하세요.
sum_axis0 = np.sum(m_datas, axis=0)

# 문제 3: 배열 결합 및 분할
# 배열 결합: 3x3 배열 A와 3x3 배열 B를 생성하고, 이 배열들을 수평으로 결합하여 하나의 3x6 배열을 만드세요.
data_A = np.random.randint(1, 10, (3, 3))
data_B = np.random.randint(1, 10, (3, 3))
h_stack = np.hstack([data_A, data_B]) # 수평으로 쌓기
# v_stack = np.vstack([data_A, data_B]) # 수직으로 쌓기
# d_stack = np.dstack([data_A, data_B]) # 깊이 방향으로 쌓기
# 배열 분할: 위에서 생성한 3x6 배열을 다시 두 개의 3x3 배열로 수평으로 분할하세요.
h_split = np.hsplit(h_stack) # 수평으로 분할
# v_split = np.hsplit(v_stack) # 수직으로 분할
# d_split = np.dsplit(d_stack) # 깊이 방향으로 분할

# 문제 4: 브로드캐스팅
# 브로드캐스팅 연습: 3x3 배열 A와 1x3 배열 B를 생성하세요. A와 B를 더한 결과를 출력하세요. 브로드캐스팅의 결과를 이해해보세요.
data_A = np.random.randint(1, 10, (3, 3))
data_B = np.random.randint(1, 10, (1, 3))
brod_add = data_A + data_B
print(brod_add)
# 조건부 연산: 1부터 10까지의 숫자로 이루어진 배열을 생성하고, 이 배열에서 5보다 큰 값을 모두 10으로 바꾸세요.
if_data = np.arange(1, 11)
c_data = np.where(if_data < 5, if_data, 10)

# 문제 5: 통계 함수 사용
# 랜덤 배열 생성: 5x5 크기의 랜덤 정수 배열을 생성하세요. 배열의 평균, 표준편차, 중위수(median)를 계산하세요.
datas = np.random.randint(1, 100, (5, 5))
mean_ = np.mean(datas)
std_ = np.std(datas)
median_ = np.median(datas)
# 최댓값 위치 찾기: 위에서 생성한 배열에서 최댓값이 있는 위치(인덱스)를 찾으세요.
max_idx = np.unravel_index(np.argmax(datas), datas.shape)

# 문제 6: 배열의 형태 변경
# 형태 변경: 1부터 12까지의 숫자로 이루어진 1차원 배열을 생성하고, 이를 3x4의 2차원 배열로 변환하세요.
datas = np.arange(1, 13).reshape(3, -1)
# 형태 변경 후 재변환: 위 배열을 다시 4x3 배열로 변환한 후, 이를 다시 1차원 배열로 변환하세요.
trans_data =  datas.T
vector_data = trans_data.flatten()