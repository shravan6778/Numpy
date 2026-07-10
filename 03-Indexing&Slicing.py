import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])

# Basic Slicing: arr[start:stop:step] 
print(arr[0:4])    # [10 20 30 40]   stop is exclusive
print(arr[2:4:1])  # [30 40]
print(arr[:5])     # [10 20 30 40 50]  start defaults to 0
print(arr[::2])    # [10 30 50]  every 2nd element
print(arr[::-1])   # [60 50 40 30 20 10]  REVERSED

# 2D Slicing 
mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat[0, :])    # [1 2 3]   entire first row
print(mat[:, 1])    # [2 5 8]   entire second column
print(mat[0:2, 1:3]) # [[2 3],[5 6]]  sub-matrix

#Fancy Indexing (uses integer array) 
print(arr[[1, 3, 5]])  # [20 40 60]  select at positions 1,3,5

#Boolean Masking
mask = arr > 30           # [False False False True True True]
print(arr[mask])          # [40 50 60]
print(arr[arr % 2 == 0]) # [10 20 30 40 50 60] — all are even here

# Combining conditions
print(arr[(arr > 20) & (arr < 50)])  # [30 40]  use & not 'and'

# Views vs Copies 
view = arr[1:4]    # slice returns a VIEW — modifying changes original!
copy = arr[1:4].copy()  # explicit copy — safe to modify
view[0] = 999
print(arr[1])  # 999 ← original was modified!