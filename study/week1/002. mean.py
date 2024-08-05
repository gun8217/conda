numbers = [10, 20, 30, 40, 50]
# 기본 평균내기 연산
average = sum(numbers) / len(numbers)
print(f"{average = }")

# sum() 함수 사용
total = 0
for number in numbers:
    total += number
average2 = total / len(numbers)
print(f"{average2 = }")

# 평균에 추가 값 더하기
point = 10
num_mean = sum(numbers) / len(numbers)
print(f"{num_mean = }")
for i in range(len(numbers)):
    numbers[i] += point
num_mean = sum(numbers) / len(numbers)
print(f"{num_mean = }")