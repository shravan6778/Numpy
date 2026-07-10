import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# reshape() 
mat2x6   = arr.reshape(2, 6)    # (2,6)  ← 2*6=12 
mat3x4   = arr.reshape(3, 4)    # (3,4)  ← 3*4=12 
mat_auto = arr.reshape(3, -1)   # (3,4)  ← -1 means "calculate for me"
print(mat_auto)

# Reshape 1D to column vector (common in ML)
col_vec = arr[:, np.newaxis]    # (12,) → (12,1)
col_vec = arr.reshape(-1, 2)   # same result
print(col_vec)

# ravel() — flatten to 1D, returns VIEW if possible 
arr_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
flat_view = arr_3d.ravel()     # [ 1  2  3  4  5  6  7  8  9 10 11 12]
                                 # Modifying flat_view may modify arr_3d!

# flatten() — always returns a COPY 
flat_copy = arr_3d.flatten()   # same result but independent copy
flat_copy[0] = 999             # does NOT affect arr_3d

# transpose() 
mat = np.array([[1,2,3],[4,5,6]])  # shape (2,3)
print(mat.T)            # shape (3,2)  — shorthand for transpose
print(mat.transpose()) # same as .T

# Common ML pattern — images to batch 
# Image: (H, W, C) → (1, H, W, C) for batch of 1
img = np.zeros((64, 64, 3))
batch = img[np.newaxis, :]     # (1, 64, 64, 3)