import numpy as np 
arr = np.array([10, 20, 30, 40, 50])
print(arr)

print(arr + 5)
print(arr * 2)

#sum of array
print(np.sum(arr))

#avg of array
print(np.mean(arr))

#max of array
print(np.max(arr))

#min of array
print(np.min(arr))

#shape of array
print(arr.shape)

#2D array
arr1 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(arr1)
print(arr1.shape)