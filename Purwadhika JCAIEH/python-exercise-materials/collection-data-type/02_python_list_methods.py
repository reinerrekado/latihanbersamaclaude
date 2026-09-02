"""
DEMO 2: Python List - Methods and Functions
=============================================================
Goal: the most commonly used list methods, plus the classic
gotcha of copying a list by reference instead of using .copy().
"""

fruits = ["apple", "cherry", "banana"]
vegetables = ["spinach"]
numbers = [1, 2, 3]

# -------------------------------------------------
# 1. Functions that work on a list
# -------------------------------------------------
print("len(numbers):", len(numbers))  # 3
print("sorted(fruits):", sorted(fruits))  # NEW list, sorted A-Z
print("fruits (unchanged):", fruits)  # sorted() does NOT modify the original

print("-" * 40)

# -------------------------------------------------
# 2. Adding items
# -------------------------------------------------
fruits.append("orange")
print("after append('orange'):", fruits)

numbers.insert(1, 1.5)  # insert 1.5 at index 1
print("after insert(1, 1.5):", numbers)

print("-" * 40)

# -------------------------------------------------
# 3. Removing items
# -------------------------------------------------
numbers.remove(1.5)  # removes by VALUE, not index
print("after remove(1.5):", numbers)

last_fruit = fruits.pop()  # removes and returns the LAST item
print("popped:", last_fruit, "| fruits now:", fruits)

vegetables.clear()
print("after clear():", vegetables)

print("-" * 40)

# -------------------------------------------------
# 4. copy() vs reference - a very common bug!
# -------------------------------------------------
vegetables = ["spinach"]

# WITHOUT .copy(): new_vegetables just POINTS to the same list
new_vegetables = vegetables
new_vegetables.append("carrot")
print("vegetables (no .copy()):", vegetables)         # ['spinach', 'carrot'] <- changed too!
print("new_vegetables:", new_vegetables)               # ['spinach', 'carrot']
print("same object?", vegetables is new_vegetables)    # True

vegetables = ["spinach"]

# WITH .copy(): new_vegetables_2 is an independent list
new_vegetables_2 = vegetables.copy()
new_vegetables_2.append("carrot")
print("vegetables (with .copy()):", vegetables)         # ['spinach'] <- unchanged
print("new_vegetables_2:", new_vegetables_2)             # ['spinach', 'carrot']
print("same object?", vegetables is new_vegetables_2)    # False

print("-" * 40)

# -------------------------------------------------
# 5. extend() vs append() - both add to the end, but differently
# -------------------------------------------------
list_A = [1, 2, 3]
list_B = [4, 5, 6]

list_B_appended = list_B.copy()
list_B_appended.append(list_A)
print("append(list_A):", list_B_appended)  # [4, 5, 6, [1, 2, 3]] <- list_A added as ONE item

list_B_extended = list_B.copy()
list_B_extended.extend(list_A)
print("extend(list_A):", list_B_extended)  # [4, 5, 6, 1, 2, 3] <- each item added individually
