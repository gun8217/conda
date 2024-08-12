from utils import *

n_students, min_val, max_val = 100, 0, 10
scores = get_randint_data(n_data=n_students, min_val=min_val, max_val=max_val, random_seed=0)
print(f"{scores = }")

unique_values, unique_cnts = unique2(scores)
print(f"{unique_values = }")
print(f"{unique_cnts = }")