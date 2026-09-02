"""
DEMO 9: Python Set Operations
=============================================================
Goal: combine and compare sets - union, intersection,
difference, symmetric difference, and subset/superset checks.
"""

A = {"a", "b", "c"}
B = {"b", "c", "d"}

print("A:", A)
print("B:", B)

print("-" * 40)

# -------------------------------------------------
# 1. union() -> everything in A or B or both
# -------------------------------------------------
print("A.union(B):", A.union(B))  # {'a', 'b', 'c', 'd'}
print("A | B     :", A | B)       # same thing, operator shorthand

# -------------------------------------------------
# 2. intersection() -> only what's in BOTH
# -------------------------------------------------
print("A.intersection(B):", A.intersection(B))  # {'b', 'c'}
print("A & B            :", A & B)

# -------------------------------------------------
# 3. difference() -> in A but NOT in B
# -------------------------------------------------
print("A.difference(B):", A.difference(B))  # {'a'}
print("A - B          :", A - B)

# -------------------------------------------------
# 4. symmetric_difference() -> in A or B, but NOT in both
# -------------------------------------------------
print("A.symmetric_difference(B):", A.symmetric_difference(B))  # {'a', 'd'}
print("A ^ B                    :", A ^ B)

print("-" * 40)

A2 = {"a", "b"}
B2 = {"a", "b", "c", "d"}
D2 = {"b", "c"}

# -------------------------------------------------
# 5. issubset() -> are ALL of A's elements also in B?
# -------------------------------------------------
print("A2.issubset(B2):", A2.issubset(B2))  # True
print("D2.issubset(B2):", D2.issubset(B2))  # True
print("B2.issubset(A2):", B2.issubset(A2))  # False

# -------------------------------------------------
# 6. issuperset() -> does A contain ALL of B's elements?
# -------------------------------------------------
print("B2.issuperset(A2):", B2.issuperset(A2))  # True
print("A2.issuperset(B2):", A2.issuperset(B2))  # False

# -------------------------------------------------
# 7. Proper subset (<) / proper superset (>)
#    "proper" means subset/superset AND not exactly equal
# -------------------------------------------------
print("A2 < B2:", A2 < B2)  # True  (A2 is a subset of B2, and they're not equal)
print("A2 < A2:", A2 < A2)  # False (same set, not a PROPER subset of itself)
