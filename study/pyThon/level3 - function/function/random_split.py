from utils import *

data = list(range(10))
print(f"{len(data) = } -> {data = }\n")

train_ds, test_ds = random_split(data, train_size=0.8)
print(f"{len(train_ds) = } -> {train_ds = }")
print(f"{len(test_ds) = } -> {test_ds = }")