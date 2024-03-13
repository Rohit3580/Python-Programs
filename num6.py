#sorting

import numpy as np

print("1D array opertaion: ")
array1 = np.array([25,12,36,48,87,65,11,2])
print("Array is:",array1)

y = np.sort(array1)
print("Y sorted array:",y)

w = np.sort(array1)[::-1]
print("Descending sort:",w)

z = np.argsort(array1)
print("Sorting index:",z)

array1.sort()
print("Exsting sorted array",array1)

print("---------------------------------------------------------------------------------")

print("2D array opratn:")

array2 = np.array([1,17,6,47,12,33,41,2,79]).reshape((3,3))
print(array2)

a = np.sort(array2)
print("Sorted array:")
print(a)

array2.sort()
print("Existing sorted array:")
print(array2)


