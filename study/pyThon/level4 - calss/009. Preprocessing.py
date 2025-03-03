from utils import RandomDataGenerator, StatisticsCalculator, Preprocessing

data_gen = RandomDataGenerator()
data = data_gen.randint(count=10)
print(f"{data = }\n")

stat_cal = StatisticsCalculator()
preprocessor = Preprocessing()

print("before mean:", stat_cal.cal_mean(data))
data_mean = preprocessor.subtraction(data)
print(f"mean subtraction: {data_mean}")
print("after mean:", stat_cal.cal_mean(data_mean))
print()
print("before mean:", stat_cal.cal_mean(data))
print("before std:", stat_cal.cal_std(data))
data_stdz = preprocessor.standardization(data)
print(f"standardization: {data_stdz}")
print("after mean:", stat_cal.cal_mean(data_stdz))
print("after std:", stat_cal.cal_std(data_stdz))
print()
print("before min:", stat_cal.cal_min(data))
print("before max:", stat_cal.cal_max(data))
data_norm = preprocessor.min_max_normalizing(data)
print(f"min_max_normalizing: {data_norm}")
print("after min:", stat_cal.cal_min(data_norm))
print("after max:", stat_cal.cal_max(data_norm))