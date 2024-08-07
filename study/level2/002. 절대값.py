import random

# 절대값 : 음수를 확인해 양수의 형태로 반환
num = int(input("절대값 : "))
if num > 5: abs_val = num
else: abs_val = -num
print(f"absolute value of {num} is {abs_val}")


######## 절대값 리스트 ###################################################
n_data = 5
# type1
data = [random.randint(-10, 10) for _ in range(n_data)]
print(f"{data}\n")

data_abs = []
for data_ in data:
    if data_ >= 0: data_abs.append(data_)
    else: data_abs.append(-data_)
print(f"{data_abs}\n")

# type2
data2 = [random.randint(-10, 10) for _ in range(n_data)]
print(f"{data2}\n")

data_abs2 = []
for data2_ in data2:
    if data2_ >= 0: abs_val2 = data2_
    else: abs_val2 = -data2_
    data_abs2.append(abs_val2)
print(data_abs2)