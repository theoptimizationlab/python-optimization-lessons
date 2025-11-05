"""
Lesson 2 – Decisions & Loops: Searching for the Best

Big idea:
Optimization = check → compare → repeat → keep the best.

This file shows:
- Boolean expressions and comparisons
- If / elif / else decision rules
- Loops over ranges and lists
- Accumulation (total / average)
- "Best-so-far" patterns for min / max and constrained choices
"""

# ---------------------------------------------------------
# 1. Boolean expressions and comparisons
# ---------------------------------------------------------

print("=== Boolean Expressions and Comparisons ===")

speed = 22
limit = 25

print("speed < limit:", speed < limit)
print("limit - speed >= 5:", limit - speed >= 5)
print("(speed <= limit) and (speed % 2 == 0):",
      (speed <= limit) and (speed % 2 == 0))
print()

# Feasibility check: is a cost within budget?
budget = 14
cost = 15
print("Cost within budget?", cost <= budget)
print()


# ---------------------------------------------------------
# 2. If / elif / else – transport rule by distance
# ---------------------------------------------------------

print("=== Transport Rule by Distance ===")

distance_miles = 3.1

if distance_miles < 1:
    print("Walk")
elif distance_miles < 2.5:
    print("Bike")
else:
    print("Bus")

print()


# ---------------------------------------------------------
# 3. Nested conditions – weather + distance
# ---------------------------------------------------------

print("=== Nested Conditions: Weather + Distance ===")

raining = True
distance = 1.8

if raining:
    if distance < 0.75:
        print("Walk")
    else:
        print("Bus")
else:
    if distance < 0.75:
        print("Walk")
    elif distance < 2.5:
        print("Bike")
    else:
        print("Bus")

print()


# ---------------------------------------------------------
# 4. Loops with range()
# ---------------------------------------------------------

print("=== Loops with range() ===")

print("range(3):")
for i in range(3):
    print(i)

print("\nrange(2, 7):")
for i in range(2, 7):
    print(i)

print("\nrange(10, 0, -2):")
for i in range(10, 0, -2):
    print(i)

print()


# ---------------------------------------------------------
# 5. Looping over lists
# ---------------------------------------------------------

print("=== Looping Over a List ===")

times = [18, 13, 16, 11]
for t in times:
    print("Route time:", t)

print()


# ---------------------------------------------------------
# 6. Accumulation pattern – total and average
# ---------------------------------------------------------

print("=== Accumulation Pattern: Total and Average ===")

scores = [72, 88, 91, 79]

total = 0
count = 0

for s in scores:
    total += s
    count += 1

average = total / count

print("Scores:", scores)
print("Total:", total)
print("Average:", average)
print()


# ---------------------------------------------------------
# 7. Best-so-far – find minimum and maximum
# ---------------------------------------------------------

print("=== Best-So-Far: Minimum Time (Fastest Route) ===")

times = [18, 13, 16, 11]

best_time = float('inf')
best_idx = -1

for i, t in enumerate(times):
    if t < best_time:
        best_time = t
        best_idx = i

print("Times:", times)
print("Best route index:", best_idx, "with", best_time, "minutes")
print()

print("=== Best-So-Far: Maximum Fun ===")

fun = [6, 9, 7, 8]

best_fun = -float('inf')
best_idx = -1

for i, f in enumerate(fun):
    if f > best_fun:
        best_fun = f
        best_idx = i

print("Fun scores:", fun)
print("Best activity index:", best_idx, "with fun =", best_fun)
print()


# ---------------------------------------------------------
# 8. Filter + best-so-far – constraints matter
# ---------------------------------------------------------

print("=== Filter + Best-So-Far: Budget Constraint ===")

prices = [5, 3, 7, 2, 9]
budget = 6

best_price = -1

for p in prices:
    if p <= budget and p > best_price:
        best_price = p

print("Prices:", prices)
print("Budget:", budget)
print("Best affordable price:", best_price)
print()

print("=== Filter + Best-So-Far: Fastest Route When Raining ===")

routes = [("walk", 14), ("bike", 9), ("bus", 8)]
raining = True

best_mode = None
best_time = float('inf')

for mode, t in routes:
    if raining and mode == "bike":
        continue
    if t < best_time:
        best_time = t
        best_mode = mode

print("Routes:", routes)
print("Raining:", raining)
print("Take:", best_mode, "Time:", best_time)
print()


# ---------------------------------------------------------
# 9. Practice suggestions
# ---------------------------------------------------------
# See the Lesson 2 handout for exercises such as:
# - Even / odd check
# - Budget "buy" or "skip" decisions
# - Transport rules for many distances
# - Average of a list of temperatures
# - Best-so-far with time, rating, and budget examples

