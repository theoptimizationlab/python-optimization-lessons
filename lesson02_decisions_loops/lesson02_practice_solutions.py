"""
Lesson 2 – Practice Problem Solutions

These are example solutions for the Lesson 2 practice problems.
Students should try the problems on their own before checking this file.
"""

# Problem 1 – Even / Odd
def even_or_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

print("Problem 1 – Even / Odd")
even_or_odd(7)
even_or_odd(22)
print()


# Problem 2 – Budget check for prices
print("Problem 2 – Budget check for prices")

budget = 20
prices = [8, 12, 5, 15, 4]

for p in prices:
    if p <= budget:
        print(p, ": buy")
    else:
        print(p, ": skip")

print()


# Problem 3 – Transport rules (raining + distance)
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


# Problem 4 – Numbers from 5 to 15 (inclusive)
print("Problem 4 – Numbers from 5 to 15")

for i in range(5, 16):
    print(i)

print()


# Problem 5 – Average temperature
print("Problem 5 – Average temperature")

temps = [59, 63, 71, 68, 64]
total = 0
count = 0

for t in temps:
    total += t
    count += 1

avg = total / count
print("Average:", avg)
print()


# Problem 6 – Mode for each distance
print("Problem 6 – Mode for each distance")

miles = [0.6, 1.1, 2.3, 3.2]

for d in miles:
    if d < 1:
        print(d, "-> Walk")
    elif d < 2.5:
        print(d, "-> Bike")
    else:
        print(d, "-> Bus")

print()


# Problem 7 – Index of fastest route
print("Problem 7 – Index of fastest route")

times = [14, 12, 17, 9, 13]
best_time = float("inf")
best_idx = -1

for i, t in enumerate(times):
    if t < best_time:
        best_time = t
        best_idx = i

print("Fastest index:", best_idx, "time:", best_time)
print()


# Problem 8 – Index of highest rating (first if tie)
print("Problem 8 – Index of highest rating")

ratings = [3, 5, 4, 5, 2]
best_val = -float("inf")
best_idx = -1

for i, r in enumerate(ratings):
    if r > best_val:
        best_val = r
        best_idx = i

print("Best index:", best_idx, "value:", best_val)
print()


# Problem 9 – Most expensive item you can afford
print("Problem 9 – Most expensive item within budget")

prices = [5, 7, 3, 6, 9]
budget = 8
best = -1

for p in prices:
    if p <= budget and p > best:
        best = p

print("Most expensive within budget:", best)
print()


# Problem 10 – Best pair under budget (challenge)
print("Problem 10 – Best pair under budget (challenge)")

items = [(3, 4), (4, 5), (6, 6), (2, 2)]  # (price, fun)
budget = 10

best_fun = -1
best_pair = None

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        price = items[i][0] + items[j][0]
        fun = items[i][1] + items[j][1]

        if price <= budget and fun > best_fun:
            best_fun = fun
            best_pair = (items[i], items[j], price, fun)

print("Best pair:", best_pair[0], "+", best_pair[1])
print("Total price:", best_pair[2], "Total fun:", best_pair[3])
print()
