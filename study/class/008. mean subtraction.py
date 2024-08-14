from utils import StatisticsCalculator

class Preprocessing:        
    def subtraction(self, data):
        stat_cal = StatisticsCalculator()
        mean = stat_cal.cal_mean(data)
        
        data = [sample - mean for sample in data]
        return data

stat_cal = StatisticsCalculator()

data = [1, 2, 3]

mean_subt = Preprocessing()
data_ = mean_subt.subtraction(data)
print(f"mean data: {data_ =}")
print("after mean :", stat_cal.cal_mean(data_))