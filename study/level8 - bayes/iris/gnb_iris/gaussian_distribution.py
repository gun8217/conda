'''
1) 다음 세 정규분포의 확률밀도함수를 그리세요.
파란색: mean = 0, std = 1
주황색: mean = 1, std = 0.5
초록색: mean = -1, std = 2

2) make_gaussian(x, mean, std) 함수를 만드세요.
'''

import numpy as np
import matplotlib.pyplot as plt

def gaussian_value(x, mean, std):
    const = 1/np.sqrt(2*np.pi*std**2)

    numerator = (x - mean)**2 # 분자
    denominator = (2 * std**2) # 분모
    exp_term = np.exp(-numerator/denominator)

    y = const * exp_term
    return y

if __name__ == '__main__':
    x = np.linspace(-5, 5, 100)
    y = gaussian_value(x, 0, 1)
    y2 = gaussian_value(x, 1, 0.5)
    y3 = gaussian_value(x, -1, 2)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, label=r'$\mu_1 = 0,\; \sigma_1 = 1$')
    ax.plot(x, y2, label=r'$\mu_2 = 1,\; \sigma_2 = 0.5$')
    ax.plot(x, y3, label=r'$\mu_3 = -1,\; \sigma_3 = 2$')
    ax.legend(fontsize=15)
    plt.show()