"""
DEMO 1: NumPy Array - Creation
=============================================================
Goal: understand what a NumPy array is, why it's faster than a
plain Python list, and the different ways to build one.

(Install NumPy first if you haven't: pip install numpy)
"""

import time
import numpy as np


# -------------------------------------------------
# 1. Why NumPy? A quick speed comparison
# -------------------------------------------------
size_of_vec = 1_000_000

def pure_python_version():
    t1 = time.time()
    x = range(size_of_vec)
    y = range(size_of_vec)
    z = [x[i] + y[i] for i in range(len(x))]
    return time.time() - t1

def numpy_version():
    t1 = time.time()
    x = np.arange(size_of_vec)
    y = np.arange(size_of_vec)
    z = x + y
    return time.time() - t1

python_time = pure_python_version()
numpy_time = numpy_version()
print(f"pure python: {round(python_time, 4)}s")
print(f"numpy:       {round(numpy_time, 4)}s")
print(f"numpy was about {round(python_time / numpy_time, 1)}x faster")
# Arrays are stored as one contiguous block of the SAME type, so NumPy
# can operate on the whole array at once instead of looping in Python.

print("-" * 40)

# -------------------------------------------------
# 2. From a Python list - 1D, 2D, 3D
# -------------------------------------------------
my_list = [1, 2, 3]
array_1d = np.array(my_list)
print("array_1d:", array_1d)

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array_2d = np.array(my_matrix)
print("array_2d:\n", array_2d)

my_list3 = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
]
array_3d = np.array(my_list3)
print("array_3d shape:", array_3d.shape)

print("-" * 40)

# -------------------------------------------------
# 3. arange(start, stop, step) - like range(), but returns an array
# -------------------------------------------------
print("np.arange(0, 10):", np.arange(0, 10))
print("np.arange(0, 11, 2):", np.arange(0, 11, 2))

print("-" * 40)

# -------------------------------------------------
# 4. zeros, ones, eye - arrays with a fixed starting value
# -------------------------------------------------
print("np.zeros(3):", np.zeros(3))
print("np.zeros((3,3)):\n", np.zeros((3, 3)))
print("np.ones((2,4)):\n", np.ones((2, 4)))
print("np.eye(4) (identity matrix):\n", np.eye(4))

print("-" * 40)

# -------------------------------------------------
# 5. linspace(start, stop, num) - "num" evenly spaced points
# -------------------------------------------------
print("np.linspace(0, 10, 3):", np.linspace(0, 10, 3))
print("np.linspace(0, 10, 5):", np.linspace(0, 10, 5))
# Compare with arange: arange spaces by STEP, linspace spaces by COUNT.

print("-" * 40)

# -------------------------------------------------
# 6. Random arrays
# -------------------------------------------------
np.random.seed(42)  # makes the "random" numbers repeatable for the demo

print("rand(5)      - uniform floats 0-1:", np.random.rand(5))
print("randn(5)     - normal dist, mean 0:", np.random.randn(5))
print("randint(1,100,5) - random ints:", np.random.randint(1, 100, 5))
