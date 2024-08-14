

class VectorCalculator:    
    def add(self, data1, data2):
        return [a + b for a, b in zip(data1, data2)]
    
    def sub(self, data1, data2):
        return [a - b for a, b in zip(data1, data2)]
    
    def scalar_mul(self, data1, data2):
        return [data1 * a for a in data2]


u = [1, 2, 3]
v = [10, 20, 30]
k = 10
vec_cal = VectorCalculator()
print(vec_cal.add(u, v))
print(vec_cal.sub(u, v))
print(vec_cal.scalar_mul(k, u))