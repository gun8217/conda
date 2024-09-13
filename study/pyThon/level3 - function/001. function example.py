import random
import datetime
import time


def say_hello_to(name):
    print(f"hellow {name}!")

name1, name2, name3 = "Yang", "Kim", "Park"
say_hello_to(name1)
print()


# 예제1
# num = int(input("Enter a number:"))

# divisors = []
# def curr_divisors(num):
#     divisor = 1
#     while divisor <= num:
#         if num % divisor == 0:
#             divisors.append(divisor)
#         divisor += 1
#     print(divisors)
        
# curr_divisors(num)


# 예제 2
# num = int(input("Enter a number:"))

# divisors = []
# def curr_divisors(num):
#     for divisor in range(1, num + 1):
#         if num % divisor == 0:
#             divisors.append(divisor)
#         divisor += 1
#     print(divisors)
        
# curr_divisors(num)


# 예제3
# def func_mean(scores):
#     mean = sum(scores) / len(scores)
#     print(mean)


# n_student = int(input("Enter a number:"))
# data1 = [random.randint(0, 100) for _ in range(n_student)]

# func_mean(data1)


# 예제4
# def max_min_value(scores):
#     max_score, min_score = None, None
#     for score in scores:
#         if max_score == None or score > max_score:
#             max_score = score
#         else:
#             min_score = score
#     print(f"{max_score = }, {min_score = }")


# n_student = int(input("student:"))
# data1 = [random.randint(0, 100) for _ in range(n_student)]
# print(data1)

# max_min_value(data1)


# 예제5
def start_end_time(type_):
    if type_ == 'start':
        print(f"START at {datetime.datetime.now()}")
    elif type_ == 'end':
        print(f"END at {datetime.datetime.now()}")
    else:
        print("WARNING: Unknown type")
    

start_end_time('start')
time.sleep(2)
start_end_time('end')
print()


# 예제6
def random_int(num):
    return [random.randint(0, 100) for _ in range(num)]


def cal_mean(data):
    mean = sum(data) / len(data)
    return mean


input_data = int(input("Enter a number:"))
scores = random_int(input_data)
print(f"{scores = }")
mean_scores = cal_mean(scores)
print(f"{mean_scores = }")


# 예제7
def sum_num(num):
    return sum(range(1, num + 1))


input_data2 = int(input("Enter a number:"))
reault = sum_num(input_data2)
print(f"{reault = }")