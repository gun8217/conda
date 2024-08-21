# 1. 숫자 합계 계산기
# num1 = int(input("input number 1:"))
# num2 = int(input("input number 2:"))

# sum = num1 + num2
# print(sum)

# 2. 문자열 반전
# str = 'hello'
# r_str = str[::-1]
# print(r_str)


# 3. 짝수 판별기
# num3 = int(input("input number:"))
# if num3 % 2 == 0:
#     print('even')
# else:
#     print('odd')

# 구구단 출력
# num4 = int(input("input number:"))
# for idx in range(9):
#     mul = num4 * (idx + 1)
#     print(f"{num4} x {idx + 1} = ", mul)

# 평균 계산기
# for _ in range(5):
#     nums = []
#     nums.append(int(input("input number:")))
# print(nums)
# print(sum(data) / len(data))

# 리스트 최대값 찾기
# import random
# datas = [random.randint(0, 100) for _ in range(10)]
# print(datas)
# max_val = None
# for data in datas:
#     if max_val == None or data > max_val:
#         max_val = data
# print(max_val)

# 문자열 길이
string = "나한테 있는"
# len_string = 0
# for char in string:
#     if char != " ":
#         len_string += 1
len_string = len([char for char in string if char != " "])
print(len_string)

# 짝수 합계
import random
datas = [random.randint(0, 100) for _ in range(10)]
print(datas)
even = 0
for data in datas:
    if data % 2 == 0:
        even += data

print(datas)

# 달력


# 팩토리얼 계산기