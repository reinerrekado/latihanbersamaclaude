"""
DEMO 4: Python Tuple - Creating Tuples
=============================================================
Goal: see when to use a tuple instead of a list - data that
should never change, like coordinates or an RGB color.
"""

# -------------------------------------------------
# 1. Data that should stay fixed: use a tuple, not a list
# -------------------------------------------------
jakarta_geolocation = (-6.200000, 106.816666)  # (latitude, longitude)
rgb_orange = (255, 128, 0)                     # (red, green, blue)

print("jakarta_geolocation:", jakarta_geolocation)
print("rgb_orange:", rgb_orange)
print("type(jakarta_geolocation):", type(jakarta_geolocation))

# Just like a list, every item has an index starting from 0
print("latitude  (index 0):", jakarta_geolocation[0])
print("longitude (index 1):", jakarta_geolocation[1])

print("-" * 40)

# -------------------------------------------------
# 2. Tuples are immutable - read only!
# -------------------------------------------------
try:
    jakarta_geolocation[0] = -6.9
except TypeError as e:
    print("Can't modify a tuple! Error:", e)
# If the data needs to change later, use a list instead.

print("-" * 40)

# -------------------------------------------------
# 3. Empty tuples - two equivalent ways to write one
# -------------------------------------------------
empty_tuple_a = tuple()
empty_tuple_b = ()
print("empty_tuple_a:", empty_tuple_a)
print("empty_tuple_b:", empty_tuple_b)

print("-" * 40)

# -------------------------------------------------
# 4. A tuple can contain another tuple (or any type)
# -------------------------------------------------
nested_tuple = (1, (2, 3, 4), ("a", "b"))
print("nested_tuple:", nested_tuple)
print("nested_tuple[1]:", nested_tuple[1])         # (2, 3, 4)
print("nested_tuple[1][0]:", nested_tuple[1][0])   # 2

# NOTE: a single-item tuple needs a trailing comma, or Python just
# treats the parentheses as regular grouping, not a tuple!
not_a_tuple = (5)
really_a_tuple = (5,)
print("type(not_a_tuple):", type(not_a_tuple))         # <class 'int'>
print("type(really_a_tuple):", type(really_a_tuple))   # <class 'tuple'>
