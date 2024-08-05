import random

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]
print(f"{scores}\n")

# 최대값
max_score = None # 0이면 음수의 값에선 error 처리
for score in scores:
    if max_score == None:
        max_score = score
    elif score > max_score:
        max_score = score
print(max_score)

# 최소값
min_score = None
for score in scores:
    if min_score == None or score < min_score:
        min_score = score
print(min_score)

# 최대/최소 index
max_score = max_score_idx = min_score = min_score_idx = None
for score_idx, score in enumerate(scores):
    if max_score == None or score > max_score:
        max_score = score
        max_score_idx = score_idx
    if min_score == None or score < min_score:
        min_score = score
        min_score_idx = score_idx

print(f"max / max idx: {max_score} / {max_score_idx}")
print(f"min / min idx: {min_score} / {min_score_idx}")