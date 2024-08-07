import random


def random_scores(unit):
    return [random.randint(0, 100) for _ in range(unit)]

def func_score():
    unit = int(input('student members : '))
    scores = random_scores(unit)
    return scores