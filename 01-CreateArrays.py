import numpy as np

# Convert any Python list/tuple into an ndarray.
# Infers dtype automatically
array=np.array([1,2,3])
print(array,"\n")

# Array filled with 0.0. Default dtype is float64.
# Shape can be int or tuple.
a_zeros=np.zeros(3)
a_zeros_3d=np.zeros((3,2))
print(a_zeros)
print(a_zeros_3d,"\n")

# Array filled with 1.0. Same rules as zeros. Useful
# for initializing weight matrices
a_ones=np.ones(3)
a_ones_3d=np.ones((3,2))
print(a_ones)
print(a_ones_3d,"\n")

# Array filled with any specific scalar value.
a_full=np.full((3,3), 7)
print(a_full,"\n")

# Like Python range() but returns an ndarray. Works
# with floats too
a_arange=np.arange(0,9,1)
print(a_arange,"\n")

# num evenly-spaced values between start and
# stop (inclusive). Used for plotting axes
a_linspace=np.linspace(0,1,10)
print(a_linspace,"\n")

# n×n identity matrix (1s on diagonal, 0s elsewhere).
# Core for linear algebra.
a_eye=np.eye(3)
print(a_eye,"\n")

# Uninitialized array (garbage values). Fastest
# allocation — use when you'll overwrite.
a_empty=np.empty((3,4))
print(a_empty)
