import random


def random_datas(num):
    return [random.randint(0, 100) for _ in range(num)]


def func_input():
    num = int(input('input number : '))
    return random_datas(num)


def func_pass_yes_no(scores, threshold):
    passY, passN = [], []
    for score in scores:
        if score >= threshold: passY.append(score)
        else: passN.append(score)
    return passY, passN


def get_randint_data(n_data, min_val, max_val, random_seed):
    random.seed(random_seed)

    data = [random.randint(min_val, max_val) for _ in range(n_data)]
    return data


# if __name__ == '__main__':
#     n_data, min_val, max_val = 10, 0, 10
#     data_ = get_randint_data(n_data=n_data, min_val=min_val, max_val=max_val, random_seed=0)
#     print(f"{data_ = }")


def func_max_min(data, max_min):
    max_val, min_val = None, None
    for data_ in data:
        if max_val == None or data_ > max_val:
            max_val = data_
        if min_val == None or data_ < min_val:
            min_val = data_

    if max_min == 'max':
        return max_val
    elif max_min == 'min':
        return min_val
    else:
        print(f"{max_min} is value error")


def cal_max_min2(data, max_min):
    target_value, target_idx = None, None

    for sample_idx, sample in enumerate(data):
        if max_min == 'max':
            if target_value == None or sample > target_value:
                target_value = sample
        elif max_min == 'min':
            if target_value == None or sample > target_value:
                target_value = sample_idx
        else:
            print(f"{max_min} is value error")


def func_descending(data, descending):
    datas = data.copy()
    datas_sort = []

    for _ in range(len(datas)):
        if descending:
            max_data, max_data_idx = datas[0], 0
            for idx in range(1, len(datas)):
                if datas[idx] > max_data:
                    max_data = datas[idx]
                    max_data_idx = idx
            
            datas_sort.append(max_data)
            datas.pop(max_data_idx)
        else:
            min_data, min_data_idx = datas[0], 0
            for idx in range(1, len(datas)):
                if datas[idx] < min_data:
                    min_data = datas[idx]
                    min_data_idx = idx
            
            datas_sort.append(min_data)
            datas.pop(min_data_idx)

    return datas_sort


def sort(data, descending):
    data_ = data.copy()
    data_sort = []

    n_data = len(data)
    for _ in range(n_data):
        if descending:
            target = cal_max_min(data_, max_min='max')
        else:
            target = cal_max_min(data_, max_min='min')

        data_sort.append(target['value'])
        data_.pop(target['idx'])

    return data_sort


def func_mean(data):
    return sum(data) / len(data)


def func_var(datas):
    mean = func_mean(datas)
    squared_var = sum((data - mean)**2 for data in datas) / len(datas)
    return squared_var


def func_std(datas):
    return func_var(datas)**0.5


def func_stdz(datas):
    mean = func_mean(datas)
    std = func_std(datas)
    return [(data - mean) / std for data in datas]


def standardization(data, verbose):
    before_mean = func_mean(data)
    before_std = func_std(data)
    
    stdz_data = func_stdz(data)
    
    after_mean = func_mean(stdz_data)
    after_std = func_std(stdz_data)
    
    if verbose:
        print(f"before: {before_mean = }")
        print(f"before: {before_std = }")
        print(f"after: {after_mean = }")
        print(f"after: {after_std = }")
        print(f"Standardized Data: {stdz_data}")
    else:
        print(f"Standardized Data: {stdz_data}")
    
    return stdz_data

# if __name__ == '__main__':
#     datas = [1, 2, 5, 11, 100]
#     max_min = func_max_min(datas, max_min=5)
#     print(max_min)

def cal_mean_std(data):
    n_data = len(data)

    mean = sum(data) / n_data
    var = sum([(sample - mean)**2 for sample in data] / n_data)
    std = var**0.5

    return mean, std


def unique(data):
    unique_values, unique_cnts = [], {}
    for data_ in data:
        if data_ not in unique_cnts:
            unique_values.append(data_)
            unique_cnts[data_] = 1
        else:
            unique_cnts[data_] += 1
        
    return unique_values, unique_cnts

def unique2(data):
    unique_dict = {}
    for sample in data:
        unique_dict[sample] == unique_dict.get(sample, 0) + 1
    return list(unique_dict.keys()), list(unique_dict.values())


def get_random_scores(n_students=20, min_val=0, max_val=100, random_seed=None):
    random.seed(random_seed)

    scores = [random.randint(min_val, max_val) for _ in range(n_students)]
    return scores

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