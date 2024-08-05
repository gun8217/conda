import random

n_students = 100
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]
print(f"{scores}\n")

scores_pass = [score for score in scores if score >= threshold]
scores_no_pass = [score for score in scores if score < threshold]
print(f"{scores_pass = }")
print(f"{scores_no_pass = }")