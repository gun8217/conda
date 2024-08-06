# for i in range(10):
#     if i % 2 == 0:
#         continue # 다음 코드는 건너뛰기
#     print(i)

import random

n_students = 20
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]
print(scores)

list = []
for score in scores:
    if score >= threshold:
        list.append(score)
print(list)

list2 = [score for score in scores if score >= threshold]
print(list2)

list3 = []
for score in scores:
    if score <= threshold:
        continue
    list3.append(score)
print(list3)