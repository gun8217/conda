# 기본 덧셈 연산
a, b = 5, 3
result1 = a + b
print(f"{result1 = }")


numbers = [10, 20, 30]
# sum() 함수 사용
result2 = sum(numbers)
print(f"{result2 = }")

# 리스트 요소 더하기
total = 0
for number in numbers:
    total += number
print(f"{total = }")

# 각각에 값에 추가 값 더하기
point = 10
point_add = [i + point for i in numbers]
print(f"{point_add = }")