numbers = []
for i in range(5):
    numbers.append(i + 1)
print(numbers)

count = 0
while count < 5:
    print(count)
    count += 1
    
number = 7
if number > 10:
    print("10보다 큽니다")
else:
    print("10보다 작습니다")
    

numbers = [10, 21, 4, 45, 66, 93]
number_dict = {}
for num in numbers:
    if num % 2 == 0:
        number_dict[num] = '짝수'
    else:
        number_dict[num] = '홀수'
print(number_dict)