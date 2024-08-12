from utils import *

datas = get_random_scores(n_data=3, min_val=0, max_val=50, random_seed=None)
print(f"{datas = }")

norm = func_norm(datas)
print(f"{norm = }")

normalizing = func_normalizing(datas)
print(f"{normalizing = }\n\n")

data_a = get_random_scores(n_data=3, min_val=0, max_val=50, random_seed=None)
data_b = get_random_scores(n_data=3, min_val=0, max_val=50, random_seed=None)
print(f"{data_a = }, {data_b = }")

dot_prod = func_dot(data_a, data_b)
print(f"{dot_prod = }")

euc_dist = func_eucDist(data_a, data_b)
print(f"{euc_dist = }")

maht_dist = func_manhDist(data_a, data_b)
print(f"{maht_dist = }\n\n")