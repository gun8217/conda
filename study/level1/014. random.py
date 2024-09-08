import random


def random_format(numbers, decimal_places=2):
    formatted_numbers = [f"{num:.{decimal_places}f}" for num in numbers]
    return formatted_numbers


data = 5; datas = [1, 2, 3, 4, 5]

print(random)

random_randint = [random.randint(0, 100) for _ in range(data)]
print(f"범위 내 출력(균일 분포) : {random_randint = }\n")

random_random = [random.random() for _ in range(data)]
formatted_numbers = random_format(random_random, decimal_places=2)
print(f"0이상 1미만 출력(균일 분포) : random_random = {formatted_numbers}\n")

random_uniform = [random.uniform(-3, 3) for _ in range(data)]
formatted_numbers = random_format(random_uniform, decimal_places=2)
print(f"범위 내 임의의 실수 출력(균등 분포) : random_uniform = {formatted_numbers}\n")

random_gauss = [random.gauss() for _ in range(data)]
formatted_numbers = random_format(random_gauss, decimal_places=2)
print(f"무작위 선택 값 출력(정규 분포) : random_gauss = {formatted_numbers}\n")

random.seed(10)
random_seed = [random.random() for _ in range(data)]
formatted_numbers = random_format(random_seed, decimal_places=2)
print(f"난수 생성기(random number generator) 초기화 : random_sedd = {formatted_numbers}\n")

random.seed() # seed값 초기화
random_choice = random.choice(formatted_numbers)
print(f"무작위 값 추출 : random_choice = {random_choice}\n")

random_shuffle = random.shuffle(datas)
print(f"무작위 값 섞기 : random_shuffle = {datas}\n")