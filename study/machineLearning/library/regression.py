import pandas as pd
import matplotlib.pyplot as plt

file = 'C:/Users/user/Documents/conda/study/machineLearning/library/regression.csv'
df = pd.read_csv(file, index_col = 0)

input_data = df['x'].values
target_data = df['y'].values

import matplotlib.pyplot as plt

#y = aX + b
def prediction(alpha, beta, x ): # alpha, beta 값을 기준으로 예측값 출력
    result = (alpha * x) + beta
    return result

alpha = 1.2
beta = -0.5

# plt.scatter(input_data,target_data)
# plt.plot(input_data, prediction(alpha, beta, input_data), color = 'red')

# target data와의 오차를 계산
def prediction_difference(alpha, beta, x, y):
    result =  (alpha * x) + beta
    diff = result - y
    return diff

def gradient_descent(alpha, beta, x, y, iterations, learning_rate):
    m = len(x)
    cost_list = []
    for _ in range(iterations):
        error = prediction_difference(alpha,beta, x, y)
        cost = (error@error) / 2*m # @ : 행렬 곱 연산

        cost_list.append(cost)
        beta = beta - learning_rate * error.mean()
        alpha = alpha - learning_rate * (error * x).mean()
        if _ % 10 == 0: # 50개 마다 그래프 출력
            print(_, '번째 이터레이션')
            plt.scatter(input_data,target_data)
            plt.plot(input_data, prediction(alpha,beta, x), color = 'red')
            plt.show()
    return alpha,beta, cost_list


# 초기값 (시작지점 지정)
alpha = -0.1
beta = -0.1
iterations = 150
learning_rate = 0.1

alpha,beta,cost_list = gradient_descent(alpha, beta, input_data,target_data, iterations, learning_rate)