

class MatrixCalculator:    
    def add(self, data1, data2):
        return [[data1_el + data2_el for data1_el, data2_el in zip(data1_row, data2_row)]
                for data1_row, data2_row in zip(data1, data2)]
    
    def sub(self, data1, data2):
        return [[data1_el - data2_el for data1_el , data2_el in zip(data1_row, data2_row)]
                for data1_row, data2_row in zip(data1, data2)]
    
    def scalar_mul(self, data1, data2):
        return [[data1 * data2_el for data2_el in data2_row]
                for data2_row in data2]


M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
N = [[10, 20, 30],
     [40, 50, 60],
     [70, 80, 90]]
k = 2
mat_cal = MatrixCalculator()
print(mat_cal.add(M, N))
print(mat_cal.sub(M, N))
print(mat_cal.scalar_mul(k, M))
print(mat_cal.scalar_mul(k, N))