from utils import get_random_scores, cal_max, cal_max_idx

def sort(data):
    scores_copy = data.copy(); scores_sort = []
    for _ in range(len(data)):        
        max_score = cal_max(scores_copy)
        max_score_idx = cal_max_idx(scores_copy)
        
        scores_sort.append(max_score)
        scores_copy.pop(max_score_idx)

    return scores_sort

n_students = 10
scores = get_random_scores(n_students)
scores_sort = sort(scores)
print(f"{scores = }")
print(f"{scores_sort = }")