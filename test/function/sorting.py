from utils import *

scores = get_random_scores()
print(f"{scores = }\n")

scores_sort_descending = sort(scores)
scores_sort_ascending = sort(scores, descending=False)
print(f"{scores_sort_descending = }")
print(f"{scores_sort_ascending = }")