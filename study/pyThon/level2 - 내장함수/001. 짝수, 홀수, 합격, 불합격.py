import random

# 홀수, 짝수
n_data = 10
data = [random.randint(0,100) for _ in range(n_data)]
print(f"{data}\n")

odd = [data_ for data_ in data if data_ % 2 != 0]
print(f"홀수 : {odd}")
even = [data_ for data_ in data if data_ % 2 == 0]
print(f"짝수 : {even}\n\n")


# 합격, 불합격
n_students = 20
scores = [random.randint(0,100) for _ in range(n_students)]
print(f"{scores}\n")

passY, passN = 0, 0
for score in scores:        
    if score >= 80:
        passY.append(score)
    else:
        passN.append(score)

print(f"합격 : {passY}")
print(f"불합격 : {passN}\n\n")