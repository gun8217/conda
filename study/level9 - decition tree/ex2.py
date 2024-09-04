import numpy as np


def entropy(probabilities):
    return -np.sum([p * np.log2(p) for p in probabilities if p > 0])


data = [
    {'Vegetation': 'riparian', 'Stream': True, 'Slope': 'moderate', 'Elevation': 300},
    {'Vegetation': 'chaparral', 'Stream': False, 'Slope': 'steep', 'Elevation': 1200},
    {'Vegetation': 'riparian', 'Stream': True, 'Slope': 'steep', 'Elevation': 1500},
    {'Vegetation': 'chaparral', 'Stream': True, 'Slope': 'steep', 'Elevation': 3000},
    {'Vegetation': 'chaparral', 'Stream': False, 'Slope': 'steep', 'Elevation': 3900},
    {'Vegetation': 'conifer', 'Stream': False, 'Slope': 'flat', 'Elevation': 4450},
    {'Vegetation': 'conifer', 'Stream': True, 'Slope': 'steep', 'Elevation': 5000}
]

all_entropy = entropy([3/7, 2/7, 2/7])
print(f'{all_entropy = }')

stream_H = entropy([4/7, 3/7])
stream_true = entropy([1/4, 3/4])
stream_false = entropy([1.0])
stream_IG = all_entropy - ((4/7 * stream_true) + (3/7 * stream_false))
print(f"{stream_IG = }")

slope_H = entropy([1/7, 5/7, 1/7])
slope_flat = entropy([1.0])
slope_steep = entropy([3/5, 2/5])
slope_moderate = entropy([1.0])
slope_IG = all_entropy - ((1/7 * slope_flat) + (5/7 * slope_steep) + (1/7 * slope_moderate))
print(f"{slope_IG = }")

# Elevation 임계점 별로 IG 구하기
elevation750_low_H = entropy([1.])
# print(f'750 미만 = {elevation750_low_H}')
elevation750_high_H = entropy([3/6, 2/6, 1/6])
# print(f'750 이상 = {elevation750_high_H}')
elevation750_IG = all_entropy - ((1/7 * elevation750_low_H) + (6/7 * elevation750_high_H))
print(f'{elevation750_IG = }')

elevation1350_low_H = entropy([1/2, 1/2])
# print(f'1350 미만 = {elevation1350_low_H}')
elevation1350_high_H = entropy([1/5, 2/5, 2/5])
# print(f'1350 이상 = {elevation1350_high_H}')
elevation1350_IG = all_entropy - ((2/7 * elevation1350_low_H) + (5/7 * elevation1350_high_H))
print(f'{elevation1350_IG = }')

elevation2250_low_H = entropy([2/3, 1/3])
# print(f'2250 미만 = {elevation2250_low_H}')
elevation2250_high_H = entropy([2/4, 2/4])
# print(f'2250 이상 = {elevation2250_high_H}')
elevation2250_IG = all_entropy - ((3/7 * elevation2250_low_H) + (4/7 * elevation2250_high_H))
print(f'{elevation2250_IG = }')

elevation4175_low_H = entropy([3/5, 2/5])
# print(f'4175 미만 = {elevation4175_low_H}')
elevation4175_high_H = entropy([1.])
# print(f'4175 이상 = {elevation4175_high_H}')
elevation4175_IG = all_entropy - ((5/7 * elevation4175_low_H) + (2/7 * elevation4175_high_H))
print(f'{elevation4175_IG = }')
print()

stream_4175_IG = entropy([3/5, 2/5]) - (3/5 * entropy([2/3, 1/3])) + (2/5 * entropy([2/2]))
print(f'{stream_4175_IG = }')
slope_4175_IG = entropy([1/5, 4/5]) - (1/5 * entropy([1/1])) + (4/5 * entropy([1/4, 3/4]))
print(f'{slope_4175_IG = }')
elevation_750_IG = entropy([1/5, 4/5]) - (1/5 * entropy([1/1])) + (4/5 * entropy([1/4, 3/4]))
print(f'{elevation_750_IG = }')
elevation_1350_IG = entropy([2/5, 3/5]) - (2/5 * entropy([1/2, 1/2])) + (3/5 * entropy([1/3, 2/3]))
print(f'{elevation_1350_IG = }')
elevation_2250_IG = entropy([3/5, 2/5]) - (3/5 * entropy([2/3, 1/3])) + (2/5 * entropy([2/2]))
print(f'{elevation_2250_IG = }')