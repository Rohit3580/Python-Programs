#Slicing

import numpy as np

print("Single Dimentional array:")
array1 = np.array([10,20,30,40,50,60,70])
print(array1)

print(array1[1:3])
print(array1[1:6:2])
print(array1[1:-3])
print(array1[::2])
print(array1[::-1])

print("----------------------------------------------------------------------------------")

print("Two Dimentional array:")

array2 = np.array([[15,16,17],[25,26,27],[35,36,37],[45,46,47]])
print(array2)
print("1--------------")

print(array2[1,])
print("2--------------")
print(array2[:,1])
print("3--------------")
print(array2[1:3,1:3])
print("4--------------")
print(array2[1:3,])
print("5---------------")
print(array2[:,1:3])
print("6--------------")
print(array2[1:3,1])