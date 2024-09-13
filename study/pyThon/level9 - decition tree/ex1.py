import numpy as np

def gini_index(probabilities):
    return 1 - np.sum(np.square(probabilities))

# 주어진 확률 분포
all = [3/7, 2/7, 2/7]               # Gini(전체)
stream = [3/7, 4/7]                 # Gini(피처1)
slope = [5/7, 1/7, 1/7]             # Gini(피처2)
elevation = [3/7, 2/7, 1/7, 1/7]    # Gini(피처3)

# Gini 지수 계산
gini_all = gini_index(all)
print(f'{gini_all = }')  # Gini(전체)

gini_stream = gini_index(stream)
print(f'{gini_stream = }')  # Gini(피처1)

gini_slope = gini_index(slope)
print(f'{gini_slope = }')  # Gini(피처2)

gini_elevation = gini_index(elevation)
print(f'{gini_elevation = }')  # Gini(피처3)

# 정보 이득 계산
ig_stream = gini_all - gini_stream
print(f'{ig_stream = }')  # IG(피처1)

ig_slope = gini_all - gini_slope
print(f'{ig_slope = }')  # IG(피처2)

ig_elevation = gini_all - gini_elevation
print(f'{ig_elevation = }')  # IG(피처3)
