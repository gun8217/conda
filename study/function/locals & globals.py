import random
from namespace_dict import *


def cal_std(scores):
    n_students = len(scores)
    score_mean = sum(scores) / n_students

    squared_diffs = [(score - score_mean)**2 for score in scores]
    score_var = sum(squared_diffs) / n_students
    score_std = score_var**0.5

    print(f"Local: {locals()}")
    print("function terminated\n")
    return score_std

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]
score_std = cal_std(scores)
print(f"Global")
print_vars(globals())