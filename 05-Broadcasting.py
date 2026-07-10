import numpy as np

# ── Rule 1: Scalar to array ───────────────────────────
arr = np.array([10, 20, 30])
print(arr + 5)     # [15 25 35]   scalar is broadcast to [5,5,5]
print(arr * 2)     # [20 40 60]

# ── Real-world: batch discount ────────────────────────
prices   = np.array([150, 170, 270, 100])
discount = 10                             # 10%
final    = prices - (prices * discount / 100)
print(final)        # [135. 153. 243.  90.]

# ── Rule 2: 1D + 2D ──────────────────────────────────
mat = np.array([[1,2,3],
                [4,5,6]])          # shape (2,3)
row = np.array([10, 20, 30])      # shape    (3,)
print(mat + row)
# row treated as (1,3), then stretched to (2,3):
# [[11 22 33]
#  [14 25 36]]

# ── Column vector vs row vector ───────────────────────
col = np.array([[10], [20]])      # shape (2,1)
row = np.array([[1, 2, 3]])      # shape (1,3)
print(col + row)
# Both broadcast to (2,3):
# [[11 12 13]
#  [21 22 23]]

# ── Incompatible (triggers ValueError) ───────────────
try:
    bad = np.array([[1,2,3]]) + np.array([[1,2]])
except ValueError as e:
    print(f"Error: {e}")         # shapes (1,3) and (1,2) not broadcastable

# ── normalize rows (common ML preprocessing) ─────────
data   = np.random.rand(4, 3)        # (4,3) — 4 samples, 3 features
means  = data.mean(axis=1, keepdims=True)   # (4,1)
stds   = data.std(axis=1, keepdims=True)    # (4,1)
normed = (data - means) / stds             # broadcasts to (4,3)


