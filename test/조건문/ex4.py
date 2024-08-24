# 문제 1: 단어 길이 계산하기
text = "OpenAI is amazing"
word_lengths = {}
words = text.split()
for word in words:
    word_lengths[word] = len(word)
print(word_lengths)

# 문제 2: 숫자의 자리수 합 구하기
nums = input("input number: ").split()
sum_of_digits = 0
for digit in nums:
    sum_of_digits += int(digit)
print(sum_of_digits)

# 문제 3: 리스트에서 최대값과 최소값 찾기
numbers = [34, 67, 12, 89, 45, 94, 23, 8]
max_v, min_v = None, None
for num in numbers:
    if max_v == None or num > max_v:
        max_v = num
    if min_v == None or num < min_v:
        min_v = num
print(f"{max_v = }, {min_v = }")

# 문제 4: 문자열 뒤집기
input_word = input("input word: ")
reversed_text = input_word[::-1]
print(reversed_text)

# 문제 5: 특정 문자 개수 세기
string = "banana"
find = "a"; count = 0
for char in string:
    if char == find:
        count += 1
print(f"'a'의 개수: {count}")

# 문제 6: 소수인지 판별하기
num = int(input("input num: "))
is_prime = True
if num < 2:
    is_prime = False
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{num}은 소수입니다.")
else:
    print(f"{num}은 소수가 아닙니다.")

# 문제 7: 리스트 내 요소들의 곱 계산하기
numbers = [2, 3, 5, 7]
num_ = 1
for num in numbers:
    num_ *= num
print(num_)