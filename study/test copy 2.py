import random

n_data = 10
data = [random.randint(1, 100) for _ in range(n_data)]
print(data)

data_abs = []
for data_ in data:
    if data_ >= 0:
        data_abs.append(data_)
    else:
        data_abs.append(-data_)
print(data_abs)

data_abs２ = []
for data２ in data:
    if data２ >= 0:
        abs_val = data2
    else:
        abs_val = data2
    data_abs2.append(abs_val)
print(data_abs２)