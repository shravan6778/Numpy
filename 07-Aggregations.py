import numpy as np

arr_1d = np.array([10, 20, 30])

# ── 1D aggregations ───────────────────────────────────
print(np.sum(arr_1d))   # 60
print(np.min(arr_1d))   # 10
print(np.max(arr_1d))   # 30
print(np.mean(arr_1d))  # 20.0
print(np.std(arr_1d))   # 8.165...
print(np.var(arr_1d))   # 66.666...  (std squared)

# ── argmin / argmax — return INDEX of min/max value ───
arr = np.array([40, 10, 30, 70, 20])
print(np.argmin(arr))   # 1  (index where value is 10)
print(np.argmax(arr))   # 3  (index where value is 70)

# ── 2D aggregations with axis ─────────────────────────
mat = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])   # shape (3,4)

print(np.sum(mat))           # 78  — all elements
print(np.sum(mat, axis=0))   # [15 18 21 24]  — shape (4,) — column sums
print(np.sum(mat, axis=1))   # [10 26 42]     — shape (3,) — row sums
print(np.mean(mat, axis=0))  # [5. 6. 7. 8.]  — column means
print(np.mean(mat, axis=1))  # [2.5 6.5 10.5] — row means
print(np.max(mat, axis=1))   # [4 8 12]       — max of each row
print(np.argmax(mat, axis=1)) # [3 3 3]       — col index of max in each row

# ── keepdims — preserve shape for broadcasting ────────
means = np.mean(mat, axis=1, keepdims=True)  # shape (3,1) not (3,)
centered = mat - means   # broadcasts: (3,4) - (3,1) → (3,4)
print(centered)