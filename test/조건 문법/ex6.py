# # 문제 1: 리스트에서 짝수와 홀수 분리하기
# numbers = [12, 7, 34, 19, 8, 5, 22]
# even, odd = [], []
# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
# print(f"짝수: {even}\n홀수: {odd}")

# # 문제 2: 문자열의 단어 개수 세기
# text = input("문자열을 입력하세요: ")
# words = text.split()
# print(len(words))

# 문제 3: 2차원 리스트에서 열의 최대값 찾기
matrix = [[5, 8, 9], [3, 10, 6], [7, 4, 11]]
for col_idx in range(len(matrix[0])):
    max_v = None
    for row in matrix:
        if max_v is None or row[col_idx] > max_v:
            max_v = row[col_idx]
    print(f"열 {col_idx + 1}의 최대값: {max_v}")

# # 문제 4: 팩토리얼 계산
# num = int(input("숫자를 입력하세요: "))
# result = 1
# for i in range(1, num + 1):
#     result *= i
# print(f"{num}! = {result}")

# # 문제 5: 숫자 리스트에서 중복 제거하기
# numbers = [2, 4, 6, 2, 8, 4, 9, 6, 1]
# num_list = []
# for num in numbers:
#     if num not in num_list:
#         num_list.append(num)
# print(num_list)

# # 문제 6: 구구단 출력하기
# num = int(input("구구단을 출력할 숫자를 입력하세요: "))
# for i in range(1, 10):
#     print(f"{num} x {i} = {num * i}")