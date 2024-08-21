import random

class RandomDataGenerator:
    def randint(self, min=0, max=10, count=5):
        return [random.randint(min, max) for _ in range(count)]
    
    def uniform(self, min=0., max=1., count=5):
        return [random.uniform(min, max) for _ in range(count)]
    
    def normal(self, mean=0, std=1, count=5):
        return [random.gauss(mean, std) for _ in range(count)]


class StatisticsCalculator:
    def cal_mean(self, data):
        return sum(data) / len(data)
    
    def cal_var(self, data):
        mean = self.cal_mean(data)
        var = sum((sample - mean)**2 for sample in data) / len(data)
        return var
    
    def cal_std(self, data):
        return self.cal_var(data)**0.5
    
    def cal_max(self, data, return_idx=False):
        target_val, target_idx = None, None
        for idx, sample in enumerate(data):
            if target_val == None or sample > target_val:
                target_val = sample
                target_idx = idx                
        if return_idx: return target_val, target_idx
        else: return target_val
    
    def cal_min(self, data, return_idx=False):
        target_val, target_idx = None, None
        for idx, sample in enumerate(data):
            if target_val == None or sample < target_val:
                target_val = sample
                target_idx = idx        
        if return_idx: return target_val, target_idx
        else: return target_val
        
        
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