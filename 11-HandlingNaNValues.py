import numpy as np

arr = np.array([1, np.nan, 3, np.nan, 5])

# Detection
print(np.isnan(arr))          # [False True False True False]
print(np.isnan(arr).sum())   # 2  — count of NaN values
print(np.isnan(arr).any())   # True — are there any?

# NaN propagation (the problem!)
print(np.mean(arr))           # nan  ← NaN ruins the result
print(np.sum(arr))            # nan

# nan-safe aggregations (the fix)
print(np.nanmean(arr))        # 3.0   (mean of [1, 3, 5])
print(np.nansum(arr))         # 9.0
print(np.nanmin(arr))         # 1.0
print(np.nanmax(arr))         # 5.0
print(np.nanstd(arr))         # 1.632...
print(np.nanvar(arr))         # 2.666...
print(np.nanmedian(arr))      # 3.0

# Replacement with nan_to_num 
arr_filled = np.nan_to_num(arr, nan=0)     # [1. 0. 3. 0. 5.]
arr_mean   = np.nan_to_num(arr, nan=np.nanmean(arr))  # impute with mean

# Boolean mask to filter NaN 
clean = arr[~np.isnan(arr)]   # [1. 3. 5.]   ~ = NOT
print(clean)

# ── Handling inf values ───────────────────────────────
arr2 = np.array([1, np.inf, 3, -np.inf, 5])
print(np.isinf(arr2))         # [False True False True False]
print(np.isfinite(arr2))      # [True False True False True]

# Replace inf with large finite values
arr_safe = np.nan_to_num(arr2, posinf=1e9, neginf=-1e9)

# ── Combined: NaN + inf check ─────────────────────────
arr3 = np.array([1, np.nan, np.inf, 4])
bad_mask = np.isnan(arr3) | np.isinf(arr3)  # [F T T F]
clean3 = arr3[~bad_mask]  