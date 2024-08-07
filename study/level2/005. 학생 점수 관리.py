import random

n_students = 20
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]
print(f"{scores}\n")

# 합격생들의 점수
scores_pass = []
for score in scores:
    if score >= threshold:scores_pass.append(score)
print(f"{scores_pass = }")

scores_pass2 = [score for score in scores if score >= threshold]
print(f"{scores_pass2 = }")


# 합격, 불합격생들의 평균 점수
passY, passN = [], []
for score in scores:
    if score >= threshold: passY.append(score)
    else: passN.append(score)
mean_py = sum(passY) / len(passY)
mean_pn = sum(passN) / len(passN)
print(f"{mean_py = }")
print(f"{mean_pn = }")