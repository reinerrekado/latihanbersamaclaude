"""
DEMO 3: NumPy Broadcasting, Arithmetic, and Math Functions
=============================================================
Goal: see how NumPy applies operations element-wise, how
broadcasting lets arrays of different shapes work together, and
tour the built-in math functions.
"""

import numpy as np

# -------------------------------------------------
# 1. Arithmetic is element-wise, not matrix math
# -------------------------------------------------
arr = np.arange(1, 10)
print("arr:", arr)
print("arr + 1:", arr + 1)     # 1 is added to EVERY element
print("1 / arr:", 1 / arr)
print("arr * arr:", arr * arr) # element-by-element, NOT matrix multiplication

print("-" * 40)

# -------------------------------------------------
# 2. Broadcasting - "stretching" a smaller array to fit a bigger one
# -------------------------------------------------
# Rule: for each dimension, sizes must match, OR one of them must be 1.
matrix = np.array([[0, 0, 0], [10, 10, 10], [20, 20, 20]])
row = np.array([0, 1, 2])
print("matrix:\n", matrix)
print("row:", row)
print("matrix + row (row is broadcast to every row of matrix):\n", matrix + row)

column = np.array([[0], [10], [20]])
print("column + np.arange(3) (both get broadcast):\n", column + np.arange(3))

print("-" * 40)

# -------------------------------------------------
# 3. Comparison operators also work element-wise -> boolean array
# -------------------------------------------------
arr = np.arange(1, 10)
print("arr > 5:", arr > 5)
print("arr[arr > 5] (boolean array as a filter):", arr[arr > 5])

print("-" * 40)

# -------------------------------------------------
# 4. Common math functions
# -------------------------------------------------
arr = np.arange(1, 6)
print("arr:", arr)
print("np.sqrt(arr):", np.sqrt(arr))
print("np.exp(arr):", np.exp(arr))
print("np.log(arr):", np.log(arr))
print("np.sin(arr):", np.sin(arr))

print("-" * 40)

# -------------------------------------------------
# 5. A few more handy functions
# -------------------------------------------------
arr = np.array([3, -1, 7, -5, 2])
print("np.where(arr > 0, arr, 0)  (replace negatives with 0):",
      np.where(arr > 0, arr, 0))

grid = np.arange(1, 7).reshape(2, 3)
print("grid:\n", grid)
print("grid.T (transpose):\n", grid.T)
print("grid.flatten():", grid.flatten())

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("np.concatenate([a, b]):", np.concatenate([a, b]))
