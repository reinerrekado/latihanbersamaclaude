"""
DEMO 2: __init__ and self
=============================================================
Goal: give each object its own initial values with __init__, and
understand what self actually refers to.
"""

# -------------------------------------------------
# 1. The problem: class-level attributes are shared by everyone
# -------------------------------------------------
class CarWithoutInit:
    type_name = "suv"
    color = "red"

car_john = CarWithoutInit()
car_emily = CarWithoutInit()

print("Without __init__, every object starts identical")
print(car_john.color)    # red
print(car_emily.color)   # red -> John never chose red!

print("-" * 40)

# -------------------------------------------------
# 2. __init__ runs automatically when an object is created
# -------------------------------------------------
# __init__ is a special method Python calls the moment we write
# Car(...). Whatever we assign to self.xxx inside it becomes that
# object's own attribute.
class Car:
    def __init__(self, type_name, fuel_capacity, engine_type, color):
        self.type_name = type_name
        self.fuel_capacity = fuel_capacity
        self.engine_type = engine_type
        self.color = color
        self.position = 0

    def honk(self):
        print("Tin! Tin!")

    def move_forward(self):
        self.position += 1

    def brake(self):
        print("brake!")

# Now each car gets its own configuration at creation time
car_john = Car(type_name="sedan", fuel_capacity=45, engine_type="petrol", color="red")
car_emily = Car(type_name="SUV", fuel_capacity=50, engine_type="petrol", color="yellow")

print("With __init__, each object can be different")
print(car_john.color)    # red
print(car_emily.color)   # yellow

print("-" * 40)

# -------------------------------------------------
# 3. What is self?
# -------------------------------------------------
# self refers to "the current object" - whichever object the
# method was called on. self.color = color inside __init__ means
# "store color on THIS object", not on the class itself.
print("self refers to the current object")
print(car_john.type_name)    # sedan  -> self was car_john here
print(car_emily.type_name)   # SUV    -> self was car_emily here

# Proof that the two objects keep separate state:
car_john.move_forward()
car_john.move_forward()
print("car_john.position =", car_john.position)     # 2
print("car_emily.position =", car_emily.position)   # 0 (unaffected)
