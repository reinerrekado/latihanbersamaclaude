"""
DEMO 3: Methods
=============================================================
Goal: add behavior to a class with methods, and trace exactly what
happens step by step when we call car_john.move_forward(10).
"""

# -------------------------------------------------
# 1. A method is a function defined inside a class
# -------------------------------------------------
# get_info() and move_forward() are methods - they describe
# behaviors that a Car object can perform.
class Car:
    def __init__(self, type_name, fuel=0):
        self.type_name = type_name
        self.fuel = fuel

    def get_info(self):
        print(self.__dict__)

    def move_forward(self, distance):
        if self.fuel > 0:
            print(f"Move {distance} km")
            self.fuel -= 1
        else:
            print("No fuel!")

car_john = Car("sedan", 40)
car_emily = Car("suv")   # fuel defaults to 0

# -------------------------------------------------
# 2. Calling a method
# -------------------------------------------------
car_john.get_info()          # {'type_name': 'sedan', 'fuel': 40}
car_john.move_forward(10)    # Move 10 km
car_emily.move_forward(10)   # No fuel!

print("-" * 40)

# -------------------------------------------------
# 3. What happens step by step when we call car_john.move_forward(10)?
# -------------------------------------------------
# 1) We call the method on the object: car_john.move_forward(10)
# 2) Python looks for move_forward inside the Car class -> found it
# 3) Python passes car_john as `self` and 10 as `distance`
# 4) Inside the method, self now refers to car_john
# 5) self.fuel is 40, so the "if" branch runs and self.fuel -= 1
# 6) The method finishes and control returns to the caller
print("Before:", car_john.fuel)   # 39 (already moved once above)
car_john.move_forward(5)          # Move 5 km
print("After:", car_john.fuel)    # 38
