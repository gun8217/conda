import random

n_students = 20
scores = [random.randint(0, 100) for _ in range(n_students)]
print(scores)

score_info = {}
# 표준편차
score_info['mean'] = sum(scores) / len(scores)
score_info['squared_mean'] = [(score - score_info['mean'])**2 for score in scores]
score_info['squared_var'] = sum(score_info['squared_mean']) / len(score_info['squared_mean'])
score_info['squared_std'] = score_info['squared_var']**0.5
print(score_info)

# 최대, 최대 인덱스, 최소, 최소 인덱스
max, max_idx, min, min_idx = None, None, None, None
for score_idx, score in enumerate(scores) :
    if max == None or score > max:
        max = score
        max_idx = score_idx

    if min == None or score < min:
        min = score
        min_idx = score_idx

print(f"{max = }, {max_idx = }")
print(f"{min = }, {min_idx = }")