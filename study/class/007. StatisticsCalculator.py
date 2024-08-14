from utils import RandomDataGenerator, StatisticsCalculator

data_gen = RandomDataGenerator()
data = data_gen.randint(count=10)
print(f"{data = }")

statistics = StatisticsCalculator()
print(f"mean:", statistics.cal_mean(data))
print(f"var:", statistics.cal_var(data))
print(f"std:", statistics.cal_std(data))
print(f"max_val:", statistics.cal_max(data))
max_val, max_idx = statistics.cal_max(data, return_idx=True)
print(f"{max_val = }, {max_idx = }")
print(f"min_val:", statistics.cal_min(data))
min_val, min_idx = statistics.cal_min(data, return_idx=True)
print(f"{min_val = }, {min_idx = }")