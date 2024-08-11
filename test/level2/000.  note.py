from module import *

# inputBox = int(input("input:"))

# # 홀수, 짝수
# if inputBox % 2 != 0: print("홀수")
# else: print("짝수")

# # 합격, 불합격
# n_students = 10
# threshold = 80
# scores = [random.randint(0, 100) for _ in range(n_students)]
# print(scores)

# passY, passN = [], []
# for score in scores:
#     if score >= threshold:
#         passY.append(score)
#     else:
#         passN.append(score)
# print(f"{passY = }")
# print(f"{passN = }")

# datas = [random.randint(-10, 10) for _ in range(10)]
# # 절대값
# abs_val2 = []
# for data in datas:
#     if data >= 0:
#         abs_val2.append(data)
#     else:
#         abs_val2.append(-data)
# print(f"{abs_val2 = }")

# # ReLU 양수 = 1, 음수 = 0
# relu = 0
# for data in datas:
#     if data > 0: relu = data
#     else: relu = 0
#     print(f"{relu = }")

# # ReLU 리스트
# reluList = [data for data in datas if data > 0]
# print(f"{reluList = }")

# 3n cycle
# num = int(input("Enter a number : "))

# if num % 3 == 0:
#     print(f"{num} is 3n")
# elif num % 3 == 1:
#     print(f"{num} is 3n + 1")
# else:
#     print(f"{num} is 3n + 2")

# 합격생들의 점수
# scores = func_input()
# print(f"{scores = }")
# pass_score = 80
# pass_list = [score for score in scores if score >= pass_score]
# print(f"{pass_list = }")

# # 합격, 불합격생들의 평균 점수
# passY, passN = [], []
# for score in scores:
#     if score >= pass_score:
#         passY.append(score)
#     else:
#         passN.append(score)
# mean_passY = func_mean(passY) if passY else 0
# mean_passN = func_mean(passN) if passN else 0
# print(f"{mean_passY = }\n{mean_passN = }")

# prime number
# num = int(input("number: "))
# divisor_list = [divisor for divisor in range(2, num) if num % divisor == 0]
# print(f"{divisor_list = }")
# if len(divisor_list) == 0:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")
    
# manhattan distance
# data_a, data_b, data_c = random_datas2(3, 3, 3)
# print(f"{data_a = }, {data_b = }, {data_c = }")
# manhattan_distance = func_manhDist(data_a, data_b, data_c)

# # datas = random_datas_multi(3, 5) # 처음부터 튜플로 호출
# # datas = (data_a, data_b, data_c) # ()로 튜플 정의
# # for idx, data_vector in enumerate(datas):
# #     print(f"Vector {idx}: {data_vector}")
# # manhattan_distance = func_manhDist(*datas) # (*)로 튜플 언패킹

# print(f"{manhattan_distance = }")

# tp, tn, fp, fn(혼동행렬)
# data_a, data_b = random_datas2(3, 3)
# print(f"{data_a = }\n{data_b = }")

# 최대값, 최소값, 각각의 index
# datas = random_datas(10)
# print(f"{datas = }")
# max_data = func_max(datas)
# min_data = func_min(datas)
# max_idx, min_idx = max_min_idx(datas)
# print(f"{max_data = }, {max_idx = }")
# print(f"{min_data = }, {min_idx = }")

# 최대, 최소 norm
datas = random_datas(10)
print(f"{datas = }")
min_norm, max_norm = min_max_norm(datas)
print(f"{min_norm = }\n{max_norm = }")