import numpy as np

def func_eucDist(u, v):
    euc_dist = np.sum((u - v)**2)**0.5
    return euc_dist


def func_manhDist(u, v):
    manh_dist = np.sum(np.abs(u - v))
    return manh_dist