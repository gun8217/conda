import numpy as np

def cal_var(data):
    return np.var(data)

data = [
    {'season': 'winter', 'work day': 'false', 'Reantals': 800},
    {'season': 'winter', 'work day': 'false', 'Reantals': 826},
    {'season': 'winter', 'work day': 'true', 'Reantals': 900},
    {'season': 'spring', 'work day': 'false', 'Reantals': 2100},
    {'season': 'spring', 'work day': 'true', 'Reantals': 4740},
    {'season': 'spring', 'work day': 'true', 'Reantals': 4900},
    {'season': 'summer', 'work day': 'false', 'Reantals': 3000},
    {'season': 'summer', 'work day': 'true', 'Reantals': 5800},
    {'season': 'summer', 'work day': 'true', 'Reantals': 6200},
    {'season': 'autumn', 'work day': 'false', 'Reantals': 2910},
    {'season': 'autumn', 'work day': 'false', 'Reantals': 2880},
    {'season': 'autumn', 'work day': 'true', 'Reantals': 2820},
]

data_1 = [800, 826, 900]
winter = cal_var(data_1)
data_2 = [2100, 4740, 4900]
spring = cal_var(data_2)
data_3 = [3000, 5800, 6200]
summer = cal_var(data_3)
data_4 = [2910, 2880, 2820]
autumn = cal_var(data_4)
season_IG = (1/4 * winter) + (1/4 * spring) + (1/4 * summer) + (1/4 * autumn)
print(season_IG)

data_5 = [900, 4740, 4900, 5800, 6200, 2820]
true_ = cal_var(data_5)
data_6 = [800, 826, 2100, 3000, 2910, 2880]
false_ = cal_var(data_6)
day_IG = (1/2 * true_) + (1/2 * false_)
print(day_IG)