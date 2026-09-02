"""
DEMO 8: break and continue
=============================================================
"""

# -------------------------------------------------
# 1. break -> stop the loop IMMEDIATELY (slide 33)
# -------------------------------------------------
print("break example: chocolate stock runs out")
money = 10
chocolate_stock = 5

while money > 0:
    print("Buying $1 Chocolate...")

    if chocolate_stock == 0:
        print("Chocolate out of stock!")
        break   # exits the while loop right away, skipping everything below

    money = money - 1
    chocolate_stock = chocolate_stock - 1

print("Loop ended. Remaining money:", money)
print("=" * 40)


# -------------------------------------------------
# 2. continue -> skip the REST of the current iteration,
#    then jump straight to the next one (slide 34)
# -------------------------------------------------
print("continue example: free chocolate on day 7")
money = 10
day = 1

while money > 0:
    print(f"Day {day}: Buying $1 Chocolate...")

    if day == 7:
        print("Free chocolate today!")
        day = day + 1
        continue   # skip the "money -= 1" and "day += 1" lines below, restart the loop

    money = money - 1
    day = day + 1

print("Loop ended. Remaining money:", money)

# -------------------------------------------------
# Common mix-up for students:
# - break  = "I'm done, EXIT the loop completely"
# - continue = "skip THIS round only, but keep looping"
# -------------------------------------------------
