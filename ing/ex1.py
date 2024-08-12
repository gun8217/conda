import random

def get_normal_data(n_data, mean, std):
    data = [random.gauss(mean, std) for _ in range(n_data)]
    return data

import statistics

n_data = 1000
data1 = get_normal_data(n_data=n_data, mean=0, std=1)
print(f"mean: {statistics.mean(data1)}, std: {statistics.stdev(data1)}")

data2 = get_normal_data(n_data=n_data, mean=10, std=5)
print(f"mean: {statistics.mean(data2)}, std: {statistics.stdev(data2)}")