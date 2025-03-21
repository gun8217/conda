import random

def get_random_scores(n_students=20, min_val=0, max_val=100):
    scores = [random.randint(min_val, max_val) for _ in range(n_students)]
    return scores

if __name__ == '__main__':
    scores = get_random_scores(n_students=10, max_val=10)
    print(f"{scores = }")

    scores = get_random_scores(n_students=30)
    print(f"{scores = }")

    scores = get_random_scores()
    print(f"{scores = }")