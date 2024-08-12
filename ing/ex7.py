import random

# random split

def random_split(data, train_size):
    data_ = data.copy()

    n_train_data = int(n_total_data * train_size)

    random.shuffle(data_)
    train_ds = data_[:n_train_data]
    test_ds = data_[n_train_data:]

    return train_ds, test_ds

n_total_data = 100
data = list(range(n_total_data))
train_ds, test_ds = random_split(data, train_size=0.8)

print(f"{train_ds = }, {test_ds = }")