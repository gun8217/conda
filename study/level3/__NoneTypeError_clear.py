def cal_max(data):
    if not data: return None
    max_score = data[0]
    for sample in data[1:]:
        if sample > max_score:
            max_score = sample
    return max_score


def cal_max_idx(data):
    max_score = cal_max(data)
    if max_score is None: return None
    for score_idx, score in enumerate(data):
        if score == max_score:
            return score_idx
    return None


def sort(data):
    scores_copy = data.copy()
    scores_sort = []
    while scores_copy:
        max_score_idx = cal_max_idx(scores_copy)
        if max_score_idx is not None:
            max_score = scores_copy[max_score_idx]
            scores_sort.append(max_score)
            scores_copy.pop(max_score_idx)
    return scores_sort


scores = [40, 10, 20, 30, 50]
scores_sort = sort(scores)
print(f"{scores_sort = }")