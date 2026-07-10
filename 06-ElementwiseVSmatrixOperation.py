import numpy as np

A = np.array([[1,2],[3,4]])   # shape (2,2)
B = np.array([[5,6],[7,8]])   # shape (2,2)

# Element-wise (*)
print(A * B)
# [[ 5 12]      ← each element multiplied separately
#  [21 32]]

# Matrix multiplication (@)
print(A @ B)
# [[19 22]      ← row·col dot products
#  [43 50]]

# Manual: A@B[0,0] = 1*5 + 2*7 = 19 ✓

# np.dot
# On 1D: inner product (scalar result)
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(np.dot(v1, v2))    # 32  (= 1*4 + 2*5 + 3*6)

# On 2D: matrix multiplication
print(np.dot(A, B))      # same as A @ B

# np.matmul — same as @ but function form
print(np.matmul(A, B))   # same as A @ B
