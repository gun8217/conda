# # 문제 1: 리스트에서 최대 두 번째로 큰 값 찾기
# numbers = [20, 34, 12, 56, 39, 56, 12]
# unique_numbers = list(set(numbers))
# unique_numbers.sort(reverse=True)
# if len(unique_numbers) > 1:
#     second_largest = unique_numbers[1]
#     print(f"두 번째로 큰 값: {second_largest}")
# else:
#     print("리스트에 두 번째로 큰 값이 없습니다.")

# # 문제 2: 문자열에서 가장 많이 등장한 문자 찾기
# text = input("문자열을 입력하세요: ")
# char_count = {}
# for char in text:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# most_common_char = max(char_count, key=char_count.get)
# print(f"가장 많이 등장한 문자: '{most_common_char}")
# print(f"등장 횟수: {char_count[most_common_char]}")

# # 문제 3: 소수(prime number) 판별하기
# number = int(input("숫자를 입력하세요: "))
# if number < 2: print("소수가 아닙니다.")
# else:
#     is_prime = True
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{number}은(는) 소수입니다.")
#     else:
#         print(f"{number}은(는) 소수가 아닙니다.")

# # 문제 4: 두 개의 문자열이 아나그램인지 확인하기
# str1 = input("첫 번째 문자열을 입력하세요: ")
# str2 = input("두 번째 문자열을 입력하세요: ")
# if sorted(str1) == sorted(str2):
#     print("두 문자열은 아나그램입니다.")
# else:
#     print("두 문자열은 아나그램이 아닙니다.")

# # 문제 5: 리스트를 역순으로 정렬하기 (정렬 함수 사용 금지)
# numbers = [5, 3, 8, 6, 7, 2]
# for i in range(len(numbers)):
#     for j in range(0, len(numbers) - i - 1):
#         if numbers[j] < numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
# print(f"역순으로 정렬된 리스트: {numbers}")

# 문제 6: 문자열 압축하기
text = input("문자열을 입력하세요: ")
compressed_text = ""
count = 1
for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        compressed_text += text[i - 1] + str(count)
        count = 1
compressed_text += text[-1] + str(count)
print(f"압축된 문자열: {compressed_text}")