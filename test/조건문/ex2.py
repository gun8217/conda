for i in range(1, 6):
    print(f"\n{i}단")
    for j in range(1, 10):
        print(f"{i} x {j} = {(i) * (j)}")
        
numbers = [10, 25, 35, 50, 45]
num_ = 0
for num in numbers:
    if num > num_:
        num_ = num
print(num_)

text = "hello"
text_ = []
for char in text:
    text_ = [char] + text_
print("".join(text_))

num1 = int(input("input num 1 :"))
num2 = int(input("input num 2 :"))
if num1 > num2:
    num1, num2 = num2, num1
num_sum = 0
for num in range(num1, num2 + 1):
    num_sum += num
print(num_sum)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# num3 = int(input("input num 3 :"))
# for idx, num in enumerate(numbers):
#     if num == num3:
#         numbers.pop(numbers[idx - 1])
# print(numbers)