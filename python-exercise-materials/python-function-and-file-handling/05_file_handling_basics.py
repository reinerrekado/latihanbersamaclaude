"""
DEMO 5: Working with External Files
=============================================================
Goal: learn how to open, write to, and read from a file, plus the
common modes ("r", "w", "a") and why the `with` statement is
preferred over manually calling .close().

Running this file creates "demo_notes.txt" in this same folder.
"""

# -------------------------------------------------
# 1. Writing to a file with open() ... close()
# -------------------------------------------------
file = open("demo_notes.txt", "w")  # "w" = write (overwrites the file)
file.write("Hello, Python!")
file.close()  # always close when you're done - frees the file up

print("Wrote to demo_notes.txt")

print("-" * 40)

# -------------------------------------------------
# 2. Reading from a file
# -------------------------------------------------
file = open("demo_notes.txt", "r")  # "r" = read (file must exist)
content = file.read()
file.close()

print("Read back:", content)

print("-" * 40)

# -------------------------------------------------
# 3. Appending instead of overwriting
# -------------------------------------------------
file = open("demo_notes.txt", "a")  # "a" = append (adds to the end)
file.write("\nWelcome!")
file.close()

with open("demo_notes.txt", "r") as file:
    print("After append:\n" + file.read())

print("-" * 40)

# -------------------------------------------------
# 4. The `with` statement - closes the file for us automatically
# -------------------------------------------------
# Instead of:
#     file = open("demo_notes.txt", "r")
#     content = file.read()
#     file.close()
# We can do:
with open("demo_notes.txt", "r") as file:
    content = file.read()
# file is already closed here, even if an error had happened above
print("Read using `with`:", content)
