# 문제 1: 리스트에서 특정 값의 인덱스 찾기
numbers = [4, 7, 9, 3, 7, 1, 6, 9, 3]
target = int(input("찾을 값을 입력하세요: "))
found = False
for num in numbers:
    if target == num:
        print(numbers.index(num))
        found = True
        break
if not found:
    print("찾을 수 없습니다")

# 문제 2: 문자열 뒤집기
text = input("문자열을 입력하세요: ")
reversed_text = text[::-1]
print(reversed_text)

# 문제 3: 두 리스트의 교집합 구하기
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list_ = [_ for _ in list1 if _ in list2]
print(list_)

# 문제 4: 피보나치 수열의 n번째 항 계산하기
n = int(input("n번째 항을 구할 숫자를 입력하세요: "))
fib = [0, 1]
for i in range(2, n):
    next_fib = fib[-1] + fib[-2]
    fib.append(next_fib)
print(f"{n}번째 항: {fib[n-1]}")

# 문제 5: 문자열에서 모음 제거하기
text = input("문자열을 입력하세요: ")
mo = "aeiou"
t_list = [char for char in text if char not in mo]
print("".join(t_list))

# 문제 6: 리스트에서 중복된 항목 제거하기
numbers = [1, 2, 3, 2, 4, 5, 4, 6, 7, 5]
num_list = list(set(numbers))
print(num_list)