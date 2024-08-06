# 내림차순 : Argsorting(index)
import random

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]
print(scores)

sort_indices = []
for _ in range(n_students):
    max_score = max_score_idx = None
    for score_idx, score in enumerate(scores):
        
        if score_idx in sort_indices:
            continue

        if max_score == None or score == max_score:
            max_score = score
            max_score_idx = score_idx
    sort_indices.append(max_score_idx)
print(f"{sort_indices = }")