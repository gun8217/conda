fib = [0, 1]
while len(fib) < 7:
    next_fib = fib[-1] + fib[-2]
    fib.append(next_fib)
print(fib)


numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = []
for data in list1:
    if data in list2 and data not in result:
        result.append(data)
print(result)


numbers = input("입력된 숫자들을 공백으로 구분하여 입력하세요: ").split()
numbers = [int(num) for num in numbers]
numbers.reverse()
print(" ".join(map(str, numbers))) 


text = "Hello World"
mo = 'aeiou'
count = 0
for char in text:
    if char in mo:
        count += 1
print(count)


num = int(input("input num : "))
for i in range(1, 10):
    print(f"{num} x {i} = {num * i}")