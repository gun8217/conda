import datetime
import time

# 함수 : snake_case, 코드의 재사용성, 함수 앞뒤 2줄씩 띄어쓰기
# def 함수명(paramiter):
# 함수 콜할때는 함수명(argument)

def hello():
    print("text1")
    print("text2")


hello()
print()

print(datetime.datetime.now())


def date_time():
    print(datetime.datetime.now())


date_time()
print()

# 처음 시간과 마지막 시간 표시의 시간 간격
def log_start_time():
    print(f"START at {datetime.datetime.now()}")
    

def log_end_time():
    print(f"END at {datetime.datetime.now()}")
    

log_start_time()
time.sleep(2)
log_end_time()
print()

# 입력 받은 이름을 출력
name = input("name:")


def say_hello_to(name):
    print(f"hellow {name}!")


say_hello_to(name)
print()


# 각각 시간, 분, 초를 구해 출력
def curr_time():
    curr_time = datetime.datetime.now()

    hour = curr_time.hour
    minute = curr_time.minute
    second = curr_time.second

    print(f"현재시각 : {hour}시 {minute}분 {second}초")


curr_time()

# 모든 약수 출력하는 함수 생성
num = int(input("Enter a number:"))


def curr_divisors():
    divisors = []; divisor = 1
    while divisor <= num:
        if num % divisor == 0:
            divisors.append(divisor)
        divisor += 1
    print(divisors)


curr_divisors()