import random

# 부동소수점 오차 해결 함수
def close_to_zero(value, epsilon=1e-10):
    return abs(value) < epsilon


def random_datas(num):
    return [random.randint(0, 100) for _ in range(num)]


def random_datas2(*datas):
    datas = [list(random.randint(0, 100) for _ in range(data)) for data in datas]
    return datas


def func_input():
    num = int(input('input number : '))
    return random_datas(num)


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


def func_norm(datas):
    return sum(data**2 for data in datas)**0.5


def func_norm_1(datas):
    norm_value = func_norm(datas)
    # ZeroDivisionError를 피하기 위해 예외 처리
    # if norm_value == 0:
    #     return [0] * len(datas)  # 제로 벡터 처리
    norm_data = [data / norm_value for data in datas]
    return func_norm(norm_data)


def func_dot(*vectors):    
    # 모든 벡터의 길이 확인
    length = len(vectors[0])
    for vector in vectors:
        if len(vector) != length:
            raise ValueError("All vectors must have the same length")
    
    # 내적 계산
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