import numpy as np
arr_1d = np.array([100, 200, 30, 40, 50])
arr_2d = np.array([[1,2,3],[4,5,6]])
arr_3d = np.array([[[1,2,3],[4,5,6]],
                   [[7,8,9],[10,11,12]]])

#returns number of dimensions as tuple
print(arr_1d.shape)
print(arr_3d.shape)

#returns number of dimensions
print(arr_2d.ndim)
print(arr_3d.ndim)

#returns total number of elements
print(arr_1d.size)
print(arr_2d.size)

#returns data type of elements
print(arr_1d.dtype)

#return bytes per element
print(arr_1d.itemsize)

#returns total memory in bytes
print(arr_1d.nbytes)
