"""
Lesson 2 – Practice Problem Solutions

These are example solutions for the Lesson 2 practice problems.
Students should try the problems on their own before checking this file.
"""

# ---------------------------------------------------------
# Problem 1 – Even / Odd
# ---------------------------------------------------------

def even_or_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


print("Problem 1 – Even / Odd")
even_or_odd(7)
even_or_odd(22)
print()  # blank line


# ---------------------------------------------------------
# Problem 2 – Budget check for prices
# ---------------------------------------------------------

print("Problem 2 – Budget check for prices")

budget = 20
prices = [8, 12, 5, 15, 4]

for p in prices:
    if p <= budget:
        print(p, ": buy")
    else:
        print(p, ": skip")

print()


# ---------------------------------------------------------
# Problem 3 – Transport rules (raining + distance)
# ---------------------------------------------------------

print("Problem 3 – Transport rules (raining + distance)")

def mode(raining, distance_miles):
    if raining:
        return "Bus"
    else:
        if distance_miles < 1:
            return "Walk"
        elif distance_miles < 2.5:
            return "Bike"
        else:
            return "Bus"


print(mode(True, 0.8))
print(mode(False, 0.6))
print(mode(False, 1.7))
print(mode(False, 3.1))
print()


# ------------
