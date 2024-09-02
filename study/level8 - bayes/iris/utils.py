import numpy as np


def gaussian_value(x, mean, std):
    # mean = np.mean(x); std = np.std(x)
    # PI = np.pi
    # fx = (1 / (np.sqrt(2 * PI) * std)) * np.exp(-0.5 * ((x - mean) / std)**2)
    # return fx

    const = 1/np.sqrt(2*np.pi*std**2)

    numerator = (x - mean)**2 # 분자
    denominator = (2 * std**2) # 분모
    exp_term = np.exp(-numerator/denominator)

    y = const * exp_term
    return y