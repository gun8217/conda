import random


def get_random_data(count=5, randomVar=random.randint, min=0, max=100, random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
    return [randomVar(min, max) for _ in range(count)]


def cal_mean(data):
    return sum(data) / len(data)


def cal_var(data):
    mean = cal_mean(data)
    var = sum((sample - mean)**2 for sample in data) / len(data)
    return var


def cal_std(data):
    return cal_var(data)**0.5


def standardization(data, verbose=False):
    before_mean, before_std = cal_mean(data), cal_std(data)

    data_ = data.copy()
    for idx, sample in enumerate(data_):
        data_[idx] = (sample - before_mean) / before_std

    after_mean, after_std = cal_mean(data_), cal_std(data_)

    if verbose:
        print(f"{before_mean = }, {before_std = }")
        print(f"{after_mean = }, {after_std = }")

    return data_


def cal_max(data):
    max_val = None
    for sample in data:
        if max_val == None or sample > max_val:
            max_val = sample
    return max_val


def cal_min(data):
    min_val = None
    for sample in data:
        if min_val == None or sample < min_val:
            min_val = sample
    return min_val


def get_data_statistics(data):
    return {
        'mean': cal_mean(data), 'var': cal_var(data), 'std': cal_std(data),
        'max': cal_max(data), 'min': cal_min(data)
    }


def max_min_idx(data):
    max_val, min_val = cal_max(data), cal_min(data)
    max_idx, min_idx = None, None
    for idx, sample in enumerate(data):
        if sample == max_val:
            max_idx = idx
        if sample == min_val:
            min_idx = idx

    return max_idx, min_idx


def cal_max_idx(data):
    max_val, max_idx = None, None
    for idx, sample in enumerate(data):
        if max_val == None or sample > max_val:
            max_val = sample
            max_idx = idx
    return max_val, max_idx


def cal_min_idx(data):
    min_val, min_idx = None, None
    for idx, sample in enumerate(data):
        if min_val == None or sample < min_val:
            min_val = sample
            min_idx = idx
    return min_val, min_idx


def cal_max_min(data, max=True):
    target_val, target_idx = None, None
    for idx, sample in enumerate(data):
        if max:
            if target_val == None or sample > target_val:
                target_val = sample
                target_idx = idx
        else:
            if target_val == None or sample < target_val:
                target_val = sample
                target_idx = idx
    return target_val, target_idx

def cal_mean_subt(data):
    mean = cal_mean(data)
    print(f"before : {mean = }")
    subt = [sample - mean for sample in data]
    print(f"{subt = }")
    mean = cal_mean(subt)
    rounded_mean = round(mean, 10)  # 소수점 10자리까지 반올림
    print(f"after : {rounded_mean = }")


def func_norm(data):
    return sum(sample**2 for sample in data)**0.5


def func_normalizing(data):
    norm = func_norm(data)
    return [sample / norm for sample in data]


def min_max_norm(data): # 스케일 통일
    data_ = data.copy()

    max_val, min_val = cal_max(data_), cal_min(data_)
    for idx, sample in enumerate(data_):
        data_[idx] = (sample - min_val) / (max_val - min_val)
    return data_


def func_eucDist(*vectors):
    results = []; n_vector = len(vectors)
    for i in range(n_vector):
        for j in range(i + 1, n_vector):
            dist = sum((a - b)**2 for a, b in zip(vectors[i], vectors[j]))**0.5
            results.append(dist)
    return results


def func_manhDist(*vectors):
    results = []; n_vector = len(vectors)
    for i in range(n_vector):
        for j in range(i + 1, n_vector):
            manh_dist = 0
            for a, b in zip(vectors[i], vectors[j]):
                diff = a - b
                abs_diff = -diff if (a - b) < 0 else diff
                manh_dist += abs_diff
            results.append(manh_dist)
    return results


def sort(data, descending=True):
    target_val, target_idx = None, None
    for idx, sample in enumerate(data):
        if descending:
            if target_val == None or sample > target_val:
                target_val += sample
                target_idx += idx
        else:
            pass


data1 = get_random_data(count=15)
print(f"{data1 = }")
print(sort(data1))


def split_scores():
    pass


def random_split():
    pass


def unique():
    pass