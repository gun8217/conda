import random

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]
print(f"{scores}\n")

max_score = None # 0 세팅은, 음수의 값은 error 처리되는걸 방지
for score in scores:
    if max_score == None:
        max_score = score
    elif score > max_score:
        max_score = score

print(max_score)

min_score = None
for score in scores:
    if min_score == None or score < min_score:
        min_score = score

print(min_score)