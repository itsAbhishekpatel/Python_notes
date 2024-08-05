import numpy as np

arr = np.array([12,3,4], ndmin=2)
arr0 = np.array(2)
arr2 = np.array([[1,2,3],[2,3,4],[1,2,3]])


# print(arr.shape)
print(arr2)
print(arr.shape)
print(arr2.dtype)
print(arr2.base)

zeroes = np.zeros((2,5))
print(zeroes)
print(zeroes.dtype)
print(zeroes.shape)

# rng = np.arange(15) give nmpuy array till n-1
# print(rng,rng.dtype)


