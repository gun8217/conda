from utils import *

n_students, min_val, max_val = 20, 0, 100
threshold = 80

scores = get_randint_data(n_data=n_students, min_val=min_val, max_val=max_val, random_seed=0)
print(f"{scores = }\n")

scores_pass, scores_no_pass = split_scores(scores, threshold)
print(f"{scores_pass = }")
print(f"{scores_no_pass = }")