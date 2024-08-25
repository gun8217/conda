import numpy as np

tensorL = np.array([1, 2, 3, 4])
tensorM = np.array([3, 4, 5, 6])

unique = np.unique(tensorL)
union = np.union1d(tensorL, tensorM)
intersection = np.intersect1d(tensorL, tensorM)
in1d = np.in1d(tensorL, tensorM)
setdiff1d = np.setdiff1d(tensorL, tensorM)
setxor1d = np.setxor1d(tensorL, tensorM)
print(f"유일한 원소 : {union}")
print(f"합집합 : {union}")
print(f"교집합 : {intersection}")
print(f"포함 여부 bool : {in1d}")
print(f"차집합 : {setdiff1d}")
print(f"대칭차집합(합 - 교) : {setxor1d}")