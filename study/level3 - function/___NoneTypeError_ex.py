from utils import get_random_scores, cal_max, cal_max_idx


def sort(data):
    data_ = data.copy(); data_sort = []
    for _ in range(n_students):
        max_score = cal_max(data_)
        max_score_idx = cal_max_idx(data_)
        
        data_sort.append(max_score)
        data_.pop(max_score_idx)
    
    return data_sort


n_students = 100
scores = get_random_scores(n_students)
scores_sort = sort(scores)
print(f"{scores = }")
print(f"{scores_sort = }")