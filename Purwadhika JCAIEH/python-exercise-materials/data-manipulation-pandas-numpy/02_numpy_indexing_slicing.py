"""
DEMO 2: NumPy Array - Attributes, Indexing, Slicing
=============================================================
Goal: inspect an array's shape/dtype, reshape it, pick out values
with indexing/slicing, and understand the "slices are views, not
copies" gotcha.
"""

import numpy as np

# -------------------------------------------------
# 1. shape, dtype, reshape
# -------------------------------------------------
arr = np.arange(0, 25)
print("arr:", arr)
print("arr.shape:", arr.shape)   # (25,) - 1D with 25 elements
print("arr.dtype:", arr.dtype)

grid = arr.reshape(5, 5)
print("reshape(5,5):\n", grid)
# reshape needs the new shape to hold the SAME number of elements
# 25 items -> 5x5 works, but 5x6 would raise a ValueError

print("reshape(-1) flattens back to 1D:", grid.reshape(-1))

print("-" * 40)

# -------------------------------------------------
# 2. max, min, argmax, argmin
# -------------------------------------------------
np.random.seed(1)
ranarr = np.random.randint(1, 100, 10)
print("ranarr:", ranarr)
print("max:", ranarr.max(), " -> at index", ranarr.argmax())
print("min:", ranarr.min(), " -> at index", ranarr.argmin())

print("-" * 40)

# -------------------------------------------------
# 3. Indexing and slicing a 1D array
# -------------------------------------------------
arr = np.arange(0, 11)
print("arr:", arr)
print("arr[8]:", arr[8])           # a single value
print("arr[1:5]:", arr[1:5])       # a range (stop is EXCLUDED)
print("arr[:5]:", arr[:5])         # from the start
print("arr[5:]:", arr[5:])         # to the end
print("arr[0:10:2]:", arr[0:10:2]) # every other element

print("-" * 40)

# -------------------------------------------------
# 4. Indexing and slicing a 2D array
# -------------------------------------------------
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print("arr_2d:\n", arr_2d)
print("arr_2d[1][0]  (row 1, col 0):", arr_2d[1][0])
print("arr_2d[1, 0]  (same thing, cleaner):", arr_2d[1, 0])
print("arr_2d[:2, 1:] (top-right 2x2 corner):\n", arr_2d[:2, 1:])
print("arr_2d[:, 2] (whole last column):", arr_2d[:, 2])

print("-" * 40)

# -------------------------------------------------
# 5. IMPORTANT: a slice is a VIEW, not a copy
# -------------------------------------------------
arr = np.arange(0, 11)
slice_of_arr = arr[0:6]
slice_of_arr[:] = 99
print("slice_of_arr after edit:", slice_of_arr)
print("original arr also changed!:", arr)
# NumPy avoids copying data for performance - editing a slice edits
# the SAME memory as the original array.

arr_copy = arr.copy()
arr_copy[:] = 0
print("arr_copy is independent, original arr unaffected:", arr)

print("-" * 40)

# -------------------------------------------------
# 6. Fancy indexing - select several indices at once, any order
# -------------------------------------------------
arr = np.arange(0, 11)
print("normal indexing, one at a time:", [arr[2], arr[5], arr[9]])
print("fancy indexing:", arr[[2, 5, 9]])
print("fancy indexing, any order:", arr[[9, 2, 5]])

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print("arr_2d[[0, 2]] (rows 0 and 2):\n", arr_2d[[0, 2]])
