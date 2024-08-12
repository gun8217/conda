from utils import *

n_students, min_val, max_val = 10, 0, 10
scores = get_randint_data(n_data=n_students, min_val=min_val, max_val=max_val, random_seed=0)
print(f"{scores = }")

score_mean, score_std = cal_mean_std(scores)
print(f"{score_mean = }, {score_std = }")