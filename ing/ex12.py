import random

def get_random_scores(scores, base_score=0):
    if base_score != 0:
        scores = [score + base_score for score in scores]
    score_mean = sum(scores) / len(scores)
    return score_mean

if __name__ == '__main__':
    scores = get_random_scores()
    print(f"{scores = }\n")

    scores = get_random_scores(base_score=10)
    print(f"{scores = }")