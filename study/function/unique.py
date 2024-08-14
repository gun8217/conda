from utils import *

scores = get_random_scores(n_data=50, min_val=0, max_val=10, random_seed=1)
print(f"{scores = }\n")

unique_values, unique_cnts = unique(scores)
print(f"{unique_values = }")
print(f"{unique_cnts = }\n")

print(unique2(scores))
print(unique2(scores, return_cnts=True))