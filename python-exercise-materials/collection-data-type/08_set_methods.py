"""
DEMO 8: Python Set - Methods and Functions
=============================================================
Goal: the most commonly used set methods for adding, removing,
and duplicating a set.
"""

favorite_movies = {"Inception", "Interstellar", "Spiderman: No Way Home", "Insidious"}
print("favorite_movies:", favorite_movies)

# -------------------------------------------------
# 1. Adding items
# -------------------------------------------------
favorite_movies.add("The Hulk")
print("after add('The Hulk'):", favorite_movies)

favorite_movies.update(["The Matrix", "Searching"])
print("after update([...]):", favorite_movies)

print("-" * 40)

# -------------------------------------------------
# 2. Removing items
# -------------------------------------------------
favorite_movies.remove("Spiderman: No Way Home")
print("after remove(...):", favorite_movies)

favorite_movies.discard("La La Land")  # not in the set, but no error!
print("after discard('La La Land') (not in set, no error):", favorite_movies)

discarded = favorite_movies.pop()  # removes a RANDOM item
print("popped (random):", discarded, "| favorite_movies now:", favorite_movies)

print("-" * 40)

# -------------------------------------------------
# 3. Duplicating and clearing
# -------------------------------------------------
movies_backup = favorite_movies.copy()
favorite_movies.clear()
print("favorite_movies after clear():", favorite_movies)
print("movies_backup (independent copy):", movies_backup)

print("len(movies_backup):", len(movies_backup))
