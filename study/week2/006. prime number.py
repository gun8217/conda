# 값이 변하지 않는 상수로서의 역할을 할 때 사용(NOT_PRIME = False)
num = int(input("IS_PRIME: "))
IS_PRIME = True
for divisor in range(2, num): # 2번부터 입력 받은 값 이전 까지 변수(divisor)에 담아라
    if num % divisor == 0: # 만약 변수 값으로 입력 받은 값을 나눴을 때 0이랑 같으면
        IS_PRIME = False # prime number는 거짓이 된다
if IS_PRIME:
    print(f"{num} is a prime number") # 입력 값이 prime number이면 출력
else:
    print(f"{num} is not a prime number") # 입력 값이 prime number 아니면 출력



######## 상수 리스트 ###################################################
num2 = int(input("divisor_list: "))
divisor_list = [divisor 
                for divisor2 in range(2, num2)
                if num2 % divisor2 == 0]
print(f"{divisor_list = }")
if len(divisor_list) == 0:
    print(f"{num2} is a prime number")
else:
    print(f"{num2} is not a prime number")