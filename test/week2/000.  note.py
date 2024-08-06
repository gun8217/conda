import random

# inputBox = int(input("input:"))

# # 홀수, 짝수
# if inputBox % 2 != 0: print("홀수")
# else: print("짝수")

# 합격, 불합격
n_students = 10
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]
print(scores)

passY, passN = [], []
for score in scores:
    if score >= threshold:
        passY.append(score)
    else:
        passN.append(score)
print(f"{passY = }")
print(f"{passN = }")

# 절대값
datas = [random.randint(-10, 10) for _ in range(10)]
viewArea = [data for data in datas if data > 0]
print(viewArea)

# ReLU 양수 = 1, 음수 = 0

# ReLU 리스트

# 3n cycle

# 합격생들의 점수

# 합격, 불합격생들의 평균 점수

# prime number

# manhattan distance

# accuracy fo binary classification

# tp, tn, fp, fn(혼동행렬)

# 최대, 최소