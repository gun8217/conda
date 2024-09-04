import numpy as np

def gini_index(probabilities):
    return 1 - np.sum(np.square(probabilities))

all = [3/7, 2/7, 2/7]

stream = [3/7, 4/7]
slope = [5/7, 1/7, 1/7]
elevation = [3/7, 2/7, 1/7, 1/7]

gini_all = gini_index(all)
print(f'{gini_all = }')
print()

gini_stream = (4/7) * gini_index([1/4, 2/4, 1/4]) + (3/7) * gini_index([2/3, 0, 1/3])
ig_stream = gini_all - gini_stream
print(ig_stream)
gini_slope = (4/7) * gini_index([2/4, 1/4, 1/4]) + (1/7) * gini_index([0, 1, 0]) + (1/7) * gini_index([0, 0, 1])
ig_slope = gini_all - gini_slope
print(ig_slope)
gini_elevation = (3/7) * gini_index([2/3, 0, 1/3]) + (1/7) * gini_index([0, 1, 0]) + (2/7) * gini_index([1/2, 1/2, 0]) + (1/7) * gini_index([0, 0, 1])
ig_elevation = gini_all - gini_elevation
print(ig_elevation)
print()


gini_stream_high = (2/3) * gini_index([1/2, 1/2]) + (1/3) * gini_index([1])
ig_stream_high = gini_index([2/3, 1/3]) - gini_stream_high
print(ig_stream_high)
gini_slope_high = (2/3) * gini_index([2/2, 0]) + (1/3) * gini_index([0, 1])
ig_slope_high = gini_index([2/3, 1/3]) - gini_slope_high
print(ig_slope_high)
print()


gini_stream_medium = (1/2) * gini_index([1]) + (1/2) * gini_index([1])
ig_stream_medium = gini_index([1/2, 1/2]) - gini_stream_medium
print(ig_stream_high)
gini_slope_medium = gini_index([1/2, 1/2])  # slope값은 동일한 값만 남음
ig_slope_medium = gini_index([1/2, 1/2]) - gini_slope_medium
print(ig_slope_medium)
print()