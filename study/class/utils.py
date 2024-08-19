import random

class RandomDataGenerator:
    def randint(self, min=0, max=10, count=5):
        return [random.randint(min, max) for _ in range(count)]
    
    def uniform(self, min=0., max=1., count=5):
        return [random.uniform(min, max) for _ in range(count)]
    
    def normal(self, mean=0, std=1, count=5):
        return [random.gauss(mean, std) for _ in range(count)]


class StatisticsCalculator1:
    def __init__(self, data):
        self.data = data

    def cal_mean(self):
        self.mean = sum(self.data) / len(self.data)
        return self.mean
    
    def cal_var(self):
        if 'mean' not in dir(self):
            self.cal_mean()
        self.var = sum((sample - self.mean)**2 for sample in self.data) / len(self.data)
        return self.var
    
    def cal_std(self):
        if 'var' not in dir(self):
            self.cal_var()
        self.std = self.var**0.5
        return self.std
    

class StatisticsCalculator:
    def __init__(self, data):
        self.data = data
        self._cal_mean_var_std()
        self._cal_min_max()

    def _cal_mean_var_std(self):
        self.mean = sum(self.data) / len(self.data)
        self.var = sum((sample - self.mean)**2 for sample in self.data) / len(self.data)
        self.std = self.var**0.5
    
    def _cal_min_max(self):
        self.max, self.max_idx = None, None
        self.min, self.min_idx = None, None
        for idx, sample in enumerate(self.data):
            if self.max == None or sample > self.max:
                self.max = sample
                self.max_idx = idx
            if self.min == None or sample < self.min:
                self.min = sample
                self.min_idx = idx

    def get_mean(self): return self.mean    
    def get_var(self): return self.var    
    def get_std(self): return self.std
    def get_max(self, return_idx=False):
        if return_idx: return f"max value:{self.max}", f"max index:{self.max_idx}"
        else: return f"max value:{self.max}"
    def get_min(self, return_idx=True):
        if return_idx: return f"min value:{self.min}", f"min index:{self.min_idx}"
        else: return f"min value:{self.min}"
        

class Preprocessing:
    def subtraction(self, data):
        stat_cal = StatisticsCalculator()
        mean = stat_cal.cal_mean(data)
        data = [sample - mean for sample in data]
        return data
            
    def standardization(self, data):
        stat_cal = StatisticsCalculator()
        mean, std = stat_cal.cal_mean(data), stat_cal.cal_std(data)
        data_processed = [(sample - mean) / std for sample in data]
        return data_processed
    
    def min_max_normalizing(self, data):
        stat_cal = StatisticsCalculator()
        max_val, min_val = stat_cal.cal_max(data), stat_cal.cal_min(data)
        data_processed = [(sample - min_val) / (max_val - min_val)
                          for sample in data]
        return data_processed
    

data = [1, 2, 3, 4, 5]
cal = StatisticsCalculator(data)

print(cal.get_max())
print(cal.get_min())