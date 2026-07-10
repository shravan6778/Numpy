import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# ── concatenate — requires same number of dims ─────────
print(np.concatenate((a, b)))          # [1 2 3 4 5 6]  (1D join)
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.concatenate((A, B), axis=0)) # [[1,2],[3,4],[5,6],[7,8]]
print(np.concatenate((A, B), axis=1)) # [[1,2,5,6],[3,4,7,8]]

# ── vstack / hstack — convenience wrappers ────────────
print(np.vstack((a, b)))  # [[1 2 3], [4 5 6]]  — row-wise (new rows)
print(np.hstack((a, b)))  # [1 2 3 4 5 6]       — column-wise (new cols)
# On 2D: vstack adds rows, hstack adds columns

# ── split ─────────────────────────────────────────────
arr = np.array([1,2,3,4,5,6])
parts = np.split(arr, 3)    # [array([1,2]), array([3,4]), array([5,6])]
p1, p2, p3 = parts            # unpack to variables

# Split at specific indices (not equal parts)
parts2 = np.split(arr, [2, 4])  # [array([1,2]), array([3,4]), array([5,6])]

# vsplit / hsplit for 2D
mat = np.array([[1,2,3,4],[5,6,7,8]])
left, right = np.hsplit(mat, 2)  # split into 2 halves by column

# ── insert ────────────────────────────────────────────
arr1 = np.array([1, 2, 3, 4])
new  = np.insert(arr1, 2, 100)   # [1 2 100 3 4]  at index 2

arr2d = np.array([[1,2],[3,4]])
new2d = np.insert(arr2d, 1, [100,200], axis=0)  # insert new row
# [[  1   2]
#  [100 200]    ← inserted at row index 1
#  [  3   4]]

# ── delete ────────────────────────────────────────────
print(np.delete(arr1, 2))              # [1 2 4]  remove index 2
print(np.delete(arr2d, 0, axis=1))    # delete first column

# ── append ────────────────────────────────────────────
print(np.append(arr1, [200, 300]))  