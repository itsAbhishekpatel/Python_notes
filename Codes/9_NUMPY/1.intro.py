import numpy as np

# declare array, you can make any sequence data into array just passing into array() function 
# belongs to a class, <class 'numpy.ndarray'>
arr_d1 = np.array([1,2,3,4,5]) # 1-D array
arr_d0 = np.array(28) # 0-D array

print(arr_d1,"Type: ",type(arr_d1),"Dimension: ", arr_d1.ndim)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# you can check th dimension using ndim 
print("Dimension:",a.ndim)
print("Dimension:",b.ndim)
print("Dimension:",c.ndim)
print("Dimension:",d.ndim)

# you can define the number of dimension in array function as well as when passing list 
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

# 2d array 
arr_2d = np.array([[3,4,5,6],[9,8,7,10]])

print(arr_2d)
print(arr_2d.shape) # retrun dimension of the array - rows and column

x = np.zeros((2,2,5))
print(x) 