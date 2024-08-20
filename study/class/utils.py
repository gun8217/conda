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
            if self.max is None:
                self.max, self.max_idx = sample, idx
                self.min, self.min_idx = sample, idx
            else:
                if sample > self.max:
                     self.max, self.max_idx = sample, idx
                if sample < self.min:
                     self.min, self.min_idx = sample, idx
                
    def get_mean(self): return self.mean    
    def get_var(self): return self.var    
    def get_std(self): return self.std
    def get_max(self, return_idx=False):
        if return_idx: return self.max, self.max_idx
        else: return self.max
    def get_min(self, return_idx=False):
        if return_idx: return self.min, self.min_idx
        else: return self.min
        

class Preprocessing:
    def __init__(self, data):
        self.data = data

        self.stat_cal = StatisticsCalculator(self.data)
        self.mean = self.stat_cal.get_mean()
    
    def mean_subtraction(self):
        mean = self.mean
        data_processed = [sample - mean for sample in self.data]
        return data_processed

    def standardization(self):
        mean = self.mean
        std = self.stat_cal.get_std()
        
        data_processed = [(sample - mean) / std for sample in self.data]
        return data_processed

    def min_max_normalizing(self):
        max_val = self.stat_cal.get_max()
        min_val = self.stat_cal.get_min()
        data_processed = [(sample - min_val) / (max_val - min_val)
                          for sample in self.data]
        return data_processed


def print_attributes(obj):
    print([attr for attr in dir(obj) if not attr.startswith('__')], '\n')
    # print_char = []
    # for attr in dir(obj):
    #     if not attr.startswith('__'):
    #         print_char.append(attr)
    # print(print_char)