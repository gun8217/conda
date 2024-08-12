from utils import *

scores = get_random_scores(n_data=5, min_val=0, max_val=100)
print(f"{scores = }\n\n")

max_val = cal_max(scores)
min_val = cal_min(scores)
max_data_idx, min_data_idx = max_min_idx(scores)
print(f"{max_val = }, {max_data_idx = }")
print(f"{min_val = }, {min_data_idx = }\n")

score_max = cal_max_min(scores)
score_min = cal_max_min(scores, max=False)
print(f"{score_max = } / {score_min = }\n")

normalizing = min_max_norm(scores)
print(f"{normalizing = }\n")