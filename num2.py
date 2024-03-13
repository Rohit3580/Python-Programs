import numpy as np

list1 =[[10,20,30],[40,50,60],[70,80,90]]

array1 = np.array(list1).reshape(3,3)
print(array1)
print("Dimension of array is:",array1.ndim)
print("Shape of array",array1.shape)
print("Size of array:",array1.size)
print("DataType of elements:",array1.dtype)
print("Size of datatype:",array1.itemsize)