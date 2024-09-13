from utils import get_random_scores, cal_max, cal_min

n_count = 10
scores = get_random_scores(n_count)
print(f"{scores}\n")

score_max, score_min = cal_max(scores), cal_min(scores)
print(f"before norm: {score_max = :.2f} / {score_min = :.2f}")
for idx, score in enumerate(scores):
    scores[idx] = (score - score_min) / (score_max - score_min)
score_max, score_min = cal_max(scores), cal_min(scores)
print(f"after norm: {score_max = :.2f} / {score_min = :.2f}")