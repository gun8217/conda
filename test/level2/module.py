import random

# 부동소수점 오차 해결 함수
def close_to_zero(value, epsilon=1e-10):
    return abs(value) < epsilon


def random_datas(num):
    return [random.randint(0, 100) for _ in range(num)]


def random_datas2(*datas):
    datas = [list(random.randint(0, 100) for _ in range(data)) for data in datas]
    return datas


def random_datas_multi(num, len):
    return [random_datas(len) for _ in range(num)]


def func_input():
    num = int(input('input number : '))
    return random_datas(num)


def func_mean(data):
    return sum(data) / len(data)


def func_manhDist(*vectors):
    results = []
    n_vectors = len(vectors)
    for i in range(n_vectors):
        for j in range(i + 1, n_vectors):
            distance = sum(a- b if (a - b) > 0 else -(a - b) for a, b in zip(vectors[i], vectors[j]))
            results.append(distance)
    
    return results


def func_max(datas):
    max_data = None # 0이면 음수의 값에선 error 처리
    for data in datas:
        if max_data == None or data > max_data:
            max_data = data
    return max_data


def func_min(datas):
    min_data = None
    for data in datas:
        if min_data == None or data < min_data:
            min_data = data
    return min_data


def max_min_idx(datas):
    max_data, min_data = func_max(datas), func_min(datas)
    max_data_idx, min_data_idx = None, None
    for idx, data in enumerate(datas):
        if data == max_data:
            max_data_idx = idx
        if data == min_data:
            min_data_idx = idx
            
    return max_data_idx, min_data_idx


def min_max_norm(datas):
    min_value, max_value = func_min(datas), func_max(datas)    
    for idx, data in enumerate(datas):
        datas[idx] = (data - min_value) / (max_value - min_value)
    min_value, max_value = func_min(datas), func_max(datas)
    
    return min_value, max_value