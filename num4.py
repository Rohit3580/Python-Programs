#indexing 

import numpy as np

print("One dimensional array example:")
array1 = np.array([10,20,30,40,50,60])
print(array1)
print("0th index:",array1[0])
print("3rd index:",array1[3])
print("-2nd index:",array1[-2])
print("-6th index:",array1[-6])

print("--------------------------------------------------------------------------------")

array2 = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(array2)
print("(1,2)index:",array2[1,2])
print("(0,)index:",array2[0,:])
print("(:,1)index:",array2[:,1])


