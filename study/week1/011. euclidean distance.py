###### 유클리드 거리 계산(두 점 사이의 직선 거리 측정) : 피타고라스 정리
point_a, point_b = [1, 2, 3], [10, 20, 30]

# for문 사용
e_dist = 0
for a, b in zip(point_a, point_b):
    e_dist += (a - b)**2
e_dist **= 0.5
print(f"{e_dist = }")

# 리스트 사용
e_dist2 = sum([(a - b)**2 for a, b in zip(point_a, point_b)])**0.5
print(f"{e_dist2 = }")