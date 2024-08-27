import numpy as np

arr = np.array([[1,4,2],
                [7,1,5],
                [6,2,10]])

print(np.argmax(arr))
print(np.argmax(arr,axis=0))
print(np.argmin(arr,axis=0))
print(np.argmax(arr,axis=1))
print(np.argmin(arr,axis=1))