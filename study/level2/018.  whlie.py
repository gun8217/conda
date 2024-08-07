import random

# 기본
while True:
    user_input = input("q to quit:")
    print(user_input)

    if user_input == 'q':
        break

# n을 입력 받으면 scores 값을 하나씩 출력하고, e를 입력하면 빠져 나와라
n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]

index = 0; list = []
while index < n_students:
    user_input = input("n(next) e(exit):")
    
    if user_input == 'e':
        break    
    elif user_input == 'n':
        # 객체 단위 출력
        # print(scores[index])
        
        # 리스트 타입 출력
        list.append(scores[index]) 
        print(list)
        
        index += 1
        
print(list)

# 약수 1을 제외한 첫 번째 값을 출력하라
num = int(input("Enter a number:"))

divisors = []; divisor = 1
while divisor <= num:
    if num % divisor == 0:
        divisors.append(divisor)
    divisor += 1
print(divisors[1])