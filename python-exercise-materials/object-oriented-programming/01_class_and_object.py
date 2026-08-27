"""
DEMO 1: Class and Object
=============================================================
Goal: see why OOP groups data + behavior together (instead of
keeping them separate like procedural code), then learn how to
define a class and create objects (instances) from it.
"""

# -------------------------------------------------
# 1. Procedural approach: data and functions are separate
# -------------------------------------------------
# Here, account_balance is just a variable floating around, and
# every function has to be told which balance to work on.
def deposit(account_balance, amount):
    return account_balance + amount

def withdraw(account_balance, amount):
    if amount <= account_balance:
        return account_balance - amount
    return account_balance

account_balance_1 = 100
account_balance_2 = 200

account_balance_1 = deposit(account_balance_1, 100)
account_balance_2 = deposit(account_balance_2, 200)

account_balance_1 = withdraw(account_balance_1, 10)
account_balance_2 = withdraw(account_balance_2, 30)

print("Procedural approach")
print("account_balance_1 =", account_balance_1)   # 190
print("account_balance_2 =", account_balance_2)   # 370

print("-" * 40)

# -------------------------------------------------
# 2. OOP approach: data and functions live together in a class
# -------------------------------------------------
# With OOP, each Account object keeps track of its own balance,
# so we don't have to pass it around to every function anymore.
class Account:
    def __init__(self, amount):
        self.balance = amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

account_1 = Account(100)
account_2 = Account(200)

account_1.deposit(100)
account_2.deposit(200)

account_1.withdraw(10)
account_2.withdraw(30)

print("OOP approach")
print("account_1.balance =", account_1.balance)   # 190
print("account_2.balance =", account_2.balance)   # 370

print("-" * 40)

# -------------------------------------------------
# 3. Defining a class: a blueprint for attributes + behaviors
# -------------------------------------------------
# A class is not a specific car - it's a general blueprint that
# describes what ANY car of this type can have and do.
class Car:
    type_name = "suv"
    fuel_capacity = 45
    engine_type = "petrol"

    def honk(self):
        pass

    def move_forward(self):
        pass

    def brake(self):
        pass

# -------------------------------------------------
# 4. An object is a specific instance created from a class
# -------------------------------------------------
# Both cars are created from the same Car blueprint, so they share
# the same attributes and behaviors, but they are still two
# separate objects.
car_john = Car()
car_emily = Car()

print("What is Object")
print(car_john.type_name)      # suv
print(car_emily.type_name)     # suv
print(car_john is car_emily)   # False -> two separate objects
