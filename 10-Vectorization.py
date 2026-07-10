import numpy as np
import time

N = 1_000_000  # 1 million elements
arr = np.random.rand(N)

# Method 1: Python loop (SLOW)
def square_loop(arr):
    result = []
    for x in arr:
        result.append(x ** 2)
    return np.array(result)

start = time.time()
result_loop = square_loop(arr)
loop_time = time.time() - start
print(f"Loop:{loop_time:.4f}s")     # ~0.35s

# ── Method 2: NumPy vectorised (FAST) ────────────────
start = time.time()
result_vec = arr ** 2                    # single C-level operation
vec_time = time.time() - start
print(f"Vectorised: {vec_time:.4f}s")     # ~0.003s  (100× faster!)

print(f"Speedup: {loop_time/vec_time:.0f}×")  # typically 100-200×

# More vectorised patterns 
# Element-wise ops — ALWAYS vectorise these
arr1 = np.random.randn(10_000)
arr2 = np.random.randn(10_000)

# Slow (loop):
# sum_sq = sum(a**2 + b**2 for a, b in zip(arr1, arr2))

# Fast (vectorised):
sum_sq = np.sum(arr1**2 + arr2**2)        # one line, very fast

# np.vectorize — NOT the same as real vectorisation! ─
def my_func(x):
    return x**2 + 2*x + 1

vfunc = np.vectorize(my_func)
result = vfunc(arr)   # Convenience wrapper — still calls Python per element!
                       # Use only for non-NumPy functions you can't rewrite

# BETTER (true vectorisation):
result = arr**2 + 2*arr + 1 