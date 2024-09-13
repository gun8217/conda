import random

def get_random_scores(n_students):
    scores = [random.randint(0, 100) for _ in range(n_students)]
    return scores


def cal_mean(data):
    mean = sum(data) / len(data)
    return mean


def cal_var(data):
    data_var = sum((data_ - cal_mean(data))**2 for data_ in data) / len(data)
    return data_var


def cal_std(data):
    data_std = cal_var(data)**0.5
    return data_std


def cal_max(data):
    max_score = None
    for sample in data:
        if max_score == None or sample > max_score:
            max_score = sample
    return max_score
    

def cal_min(data):
    min_score = None
    for sample in data:
        if min_score == None or sample < min_score:
            min_score = sample
    return min_score


def get_data_statisics(data):
    stat_dict = {
        'mean': cal_mean(data),'var': cal_var(data),'std': cal_std(data),
        'max': cal_max(data),'min': cal_min(data)
    }
    return stat_dict


def cal_max_idx(data):
    max_score, max_score_idx = cal_max(data), None
    for score_idx, score in enumerate(data):
        if max_score == None or score > max_score:
            max_score = score
            max_score_idx = score_idx
    return max_score_idx


def standardization(data):
    data_ = data.copy()
    
    mean = cal_mean(data_)
    std = cal_std(data_)
    
    for data_idx, data in enumerate(data_):
        data_[data_idx] = (data - mean) / std
    
    mean = cal_mean(data_)
    std = cal_std(data_)
    
    return std


def min_max_norm(data):
    data_ = data.copy()
    
    max_val = cal_max(data)
    min_val = cal_min(data)
    
    for idx, data in enumerate(data_):
        data_[idx] = (data - min_val) / (max_val - min_val)
    
    data_ = [f"{data:.2f}" for data in data_]
    
    return data_


if __name__ == '__main__':
    n_students = 10
    scores = get_random_scores(n_students)
    
    print('\n', get_data_statisics(scores), '\n')
    
    stdz = standardization(scores)
    print(f"{stdz = }\n")

    norm_data = min_max_norm(scores)
    print(f"{norm_data = }\n")
    