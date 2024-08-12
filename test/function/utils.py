import random


def get_random_scores(n_data=10, min_val=0, max_val=10, random_seed=None):
    random.seed(random_seed)

    scores = [random.randint(min_val, max_val) for _ in range(n_data)]
    return scores


def cal_mean(data):
    return sum(data) / len(data)


def cal_var(data):
    mean = cal_mean(data)
    squared_diffs = [(sample - mean) ** 2 for sample in data]
    var = cal_mean(squared_diffs)
    return var


def cal_std(data):
    return cal_var(data)**0.5


def standardization(data, verbose):
    n_data = len(data)

    mean = sum(data) / n_data
    var = sum([(sample - mean)**2 for sample in data]) / n_data
    std = var**0.5

    data_ = data.copy()
    for sample_idx, sample in enumerate(data_):
        data_[sample_idx] = (sample - mean) / std

    if verbose:
        print(f"===== Before Standardization ====")
        print(f"{mean = } / {std = }\n")

        mean = sum(data_) / n_data
        var = sum([(sample - mean) ** 2 for sample in data_]) / n_data
        std = var ** 0.5
        print(f"===== After Standardization ====")
        print(f"{mean = } / {std = }\n")
    return data_


def cal_mean_subt(data):
    data_mean = cal_mean(data)
    for idx in range(len(data)):
        data[idx] -= data_mean    
    data_mean = cal_mean(data)
    return data_mean


def func_norm(datas):
    return sum(data**2 for data in datas)**0.5


def func_normalizing(datas):
    norm_value = func_norm(datas)
    # ZeroDivisionError를 피하기 위해 예외 처리
    # if norm_value == 0:
    #     return [0] * len(datas)  # 제로 벡터 처리
    norm_data = [data / norm_value for data in datas]
    return func_norm(norm_data)


def func_dot(*vectors):
    for i in range(len(vectors) - 1):
        for j in range(i + 1, len(vectors)):
            result = sum(a * b for a, b in zip(vectors[i], vectors[j]))        
    return result


def func_eucDist(*vectors):
    results = []
    n_vectors = len(vectors)
    for i in range(n_vectors):
        for j in range(i + 1, n_vectors):
            distance = sum((a - b)**2 for a, b in zip(vectors[i], vectors[j]))**0.5
            results.append(distance)    
    return results


def func_manhDist(*vectors):
    results = []
    n_vectors = len(vectors)
    for i in range(n_vectors):
        for j in range(i + 1, n_vectors):
            distance = sum(a- b if (a - b) > 0 else -(a - b) for a, b in zip(vectors[i], vectors[j]))
            results.append(distance)    
    return results


def cal_max(data):
    max_data = None # 0이면 음수의 값에선 error 처리
    for sample in data:
        if max_data == None or sample > max_data:
            max_data = sample
    return max_data


def cal_min(data):
    min_data = None
    for sample in data:
        if min_data == None or sample < min_data:
            min_data = sample
    return min_data


def max_min_idx(data):
    max_data, min_data = cal_max(data), cal_min(data)
    max_data_idx, min_data_idx = None, None
    for idx, sample in enumerate(data):
        if sample == max_data:
            max_data_idx = idx
        if sample == min_data:
            min_data_idx = idx
    return max_data_idx, min_data_idx


def min_max_norm(data):
    data_ = data.copy()

    data_max, data_min = cal_max(data_), cal_min(data_)
    for idx, sample in enumerate(data_):
        data_[idx] = (sample - data_min) / (data_max - data_min)    
    return data_


def get_data_statistics(data):
    stat_dict = {
        'mean': cal_mean(data), 'var': cal_var(data), 'std': cal_std(data),
        'max': cal_max(data), 'min': cal_min(data)
    }
    return stat_dict


def cal_max_idx(data):
    max_data, max_data_idx = None, None
    for idx, sample in enumerate(data):
        if max_data == None or sample > max_data:
            max_data = sample
            max_data_idx = idx
    return max_data_idx


def cal_min_idx(data):
    min_data, min_data_idx = None, None
    for idx, sample in enumerate(data):
        if min_data == None or sample < min_data:
            min_data = sample
            min_data_idx = idx
    return min_data_idx


def sort(data, descending=True):
    data_ = data.copy()
    data_sort = []

    n_data = len(data)
    for _ in range(n_data):
        target_value, target_idx = cal_max_min(data_, max=descending)
        data_sort.append(target_value)
        data_.pop(target_idx)
    return data_sort


def get_randint_data(n_data, min_val, max_val, random_seed):
    random.seed(random_seed)
    data = [random.randint(min_val, max_val) for _ in range(n_data)]
    return data

def cal_max_min(data, max=True):
    target_value, target_idx = None, None
    for sample_idx, sample in enumerate(data):
        if max:
            if target_value == None or sample > target_value:
                target_value = sample
                target_idx = sample_idx
        else:
            if target_value == None or sample < target_value:
                target_value = sample
                target_idx = sample_idx
    return target_value, target_idx


def split_scores(scores, threshold):
    scores_pass, scores_no_pass = [], []
    for score in scores:
        if score >= threshold: scores_pass.append(score)
        else: scores_no_pass.append(score)
    return scores_pass, scores_no_pass


def random_split(data, train_size):
    data_ = data.copy()
    n_total_data = len(data)
    n_train_data = int(train_size * n_total_data)

    random.shuffle(data_)
    train_ds = data_[:n_train_data]
    test_ds = data_[n_train_data:]
    return train_ds, test_ds


def unique(data):
    unique_dict = {}
    for sample in data:
        unique_dict[sample] = unique_dict.get(sample, 0) + 1
    return list(unique_dict.keys()), list(unique_dict.values())


if __name__ == '__main__':
    data = [1, 2, 3]
    mean = cal_mean(data)
    var = cal_var(data)
    print(f"{mean = }, {var = }")