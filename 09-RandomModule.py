import numpy as np

# ── Seed — reproducibility is ESSENTIAL in ML ──────────
np.random.seed(42)   # same seed = same random numbers every run

# ── rand — uniform [0,1) ──────────────────────────────
print(np.random.rand(3))         # [0.374 0.950 0.731]
print(np.random.rand(2,3))      # 2×3 matrix of [0,1) values

# ── randn — standard normal N(0,1) ───────────────────
print(np.random.randn(4))        # ~[-1.5, 0.6, 1.2, -0.3]
# To get N(mu, sigma): mu + sigma * randn()
custom = 5 + 2 * np.random.randn(100)  # mean=5, std=2

# ── randint — random integers ────────────────────────
print(np.random.randint(0, 10, 5))     # [7 3 1 9 0]  — 5 ints in [0,10)
print(np.random.randint(1, 7, (3,3)))  # 3×3 dice roll matrix

# ── choice — sample from array ────────────────────────
arr = np.array([10, 20, 30, 40, 50])
print(np.random.choice(arr, 3))                  # [30 10 40] without replacement by default
print(np.random.choice(arr, 5, replace=True))   # [20 10 10 40 30] with replacement
print(np.random.choice(arr, 3,
      p=[0.1,0.1,0.5,0.1,0.2]))              # weighted sampling

# ── shuffle — in-place, no return value! ─────────────
data = np.array([1,2,3,4,5])
np.random.shuffle(data)   # modifies data in-place
print(data)               # [3 1 4 2 5] (random order)