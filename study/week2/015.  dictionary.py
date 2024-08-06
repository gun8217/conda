items = {'item1':1, 'item2':2, 'item3':3, 'item4':4}
print(type(items))

print(items['item3'])

items['item10'] = 10
print(f"{items}\n")


import random

n_students = 20
scores = [random.randint(0, 100) for _ in range(n_students)]
print(scores)

max_min_dict = {'max':None, 'max_idx':None, 'min':None, 'max_idx':None}

for score_idx, score in enumerate(scores) :
    if max_min_dict['max'] == None or score > max_min_dict['max']:
        max_min_dict['max'] = score
        max_min_dict['max_idx'] = score_idx

    if max_min_dict['min'] == None or score < max_min_dict['min']:
        max_min_dict['min'] = score
        max_min_dict['min_idx'] = score_idx

print(f"{max_min_dict['max'] = }")
print(f"{max_min_dict['max_idx'] = }")
print(f"{max_min_dict['min'] = }")
print(f"{max_min_dict['min_idx'] = }")