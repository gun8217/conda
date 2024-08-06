
keys = ['a', 'b', 'c', 'd', 'e']
values = [i for i in range(5)]
print(keys)
print(values, '\n')

test_dic = {key2: value for key2, value in zip(keys, values)}
print(test_dic, '\n\n')



import random

n_students = 100
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]

score_dict = {key: 0 for key in ['pass sum', 'no_pass_sum', 'pass_cnt', 'no_pass_cnt']}
print(score_dict)

keys = ['pass sum', 'no_pass_sum', 'pass_cnt', 'no_pass_cnt']
score_dict = {key: 0 for key in keys}
print(score_dict)

for score in scores:
    if score >= threshold:
        score_dict['pass sum'] += score
        score_dict['pass_cnt'] += 1
    else:
        score_dict['no_pass_sum'] += score
        score_dict['no_pass_cnt'] += 1
        
print(f"{score_dict['pass sum'] = }")
print(f"{score_dict['pass_cnt'] = }")
print(f"{score_dict['no_pass_sum'] = }")
print(f"{score_dict['no_pass_cnt'] = }")