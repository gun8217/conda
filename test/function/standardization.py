from utils import *

scores1 = get_random_scores(n_data=3, min_val=0, max_val=10, random_seed=1)
print(f"get_random_scores : {scores1 = }")

mean = cal_mean(scores1)
print(f"cal_mean : {mean}")

var = cal_var(scores1)
print(f"cal_var : {var}")

std = cal_std(scores1)
print(f"cal_std : {std}\n\n")

scores_stdz = standardization(scores1, verbose=True)
print(f"{scores_stdz = }")