"""
DEMO 3: Namespace and Scope
=============================================================
Goal: understand where a name "lives" and where it can be accessed
from - global vs local variables, and the global keyword.
"""

# -------------------------------------------------
# 1. Global variable vs local variable
# -------------------------------------------------
name = "Alice"  # global variable - created outside any function

def greet():
    message = "Halo!"  # local variable - only exists inside greet()
    print(message)
    print(name)  # global variables ARE accessible inside a function

greet()
print(name)  # fine - name is global

try:
    print(message)  # NameError - message only exists inside greet()
except NameError as e:
    print("Error:", e)

print("-" * 40)

# -------------------------------------------------
# 2. Reading a global variable inside a function is fine...
# -------------------------------------------------
position = 0

def if_move_forward():
    next_position = position + 1  # just READING position, no problem
    print(f"Position if moved: {next_position}")

if_move_forward()  # Position if moved: 1
print("position is still:", position)  # 0 - untouched

print("-" * 40)

# -------------------------------------------------
# 3. ...but MODIFYING a global variable needs the global keyword
# -------------------------------------------------
def move_forward():
    global position
    position += 1
    print("Moved forward")

move_forward()
print("position after move_forward():", position)  # 1

print("-" * 40)

# -------------------------------------------------
# 4. Forgetting `global` while modifying raises UnboundLocalError
# -------------------------------------------------
def move_forward_broken():
    position += 1  # Python treats this as a NEW local variable,
    print("Moved forward")  # but it's used before being assigned

try:
    move_forward_broken()
except UnboundLocalError as e:
    print("Error:", e)
