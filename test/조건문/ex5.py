# # 문제 1: 숫자의 합 계산하기
# nums = input("input numbers(space): ").split()
# sum_ = 0
# for num in nums:
#     sum_ += int(num)
# print(f"합: {sum_}")

# # 문제 2: 숫자의 자리수 합 구하기
# num = int(input("input number: "))
# result = 1
# for i in range(1, num + 1, 1):
#     result *= i
# print(f"{num}! = {result}")

# # 문제 3: 리스트 내에서 특정 값 찾기
# numbers = [10, 25, 30, 45, 50]
# num = int(input("input number: "))
# if num in numbers:
#     print(numbers.index(num))
# else:
#     print("찾을 수 없습니다")

# 문제 4: 문자열에서 특정 문자 제거하기
text = "Hello World".lower()
new_text = ""
for char in text:
    if char != "l":
        new_text += char
print(new_text)

# 문제 5: 2차원 리스트에서 특정 값 찾기
matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
num = int(input("input number: "))
found = False
for m_idx, shape in enumerate(matrix):
    for s_idx, num_ in enumerate(shape):
        if num == num_:
            print(f"{m_idx}, {s_idx}")
            found = True
            break
    if found:
        break
if not found:
    print("찾을 수 없습니다")

# 문제 6: 역삼각형 별 찍기
num = int(input("input number: "))
for i in range(num, 0, -1):
    mark = "*"
    star = mark*i
    print(star)
    # print("*" * i)