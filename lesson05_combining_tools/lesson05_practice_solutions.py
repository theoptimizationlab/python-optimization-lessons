"""
Lesson 5 – Practice Problem Solutions

These are example solutions for the Lesson 5 practice problems.
"""

# ---------------------------------------------------------
# 1. Budget picker
# ---------------------------------------------------------

print("Problem 1 – Budget picker")

prices = [11, 4, 8, 3, 12]
budget = 9

best_price = float("inf")
best_idx = -1

for i, p in enumerate(prices):
    if p <= budget and p < best_price:
        best_price = p
        best_idx = i

if best_idx == -1:
    print("Nothing affordable.")
else:
    print("Cheapest within budget is item", best_idx, "at price", best_price)

print()


# ---------------------------------------------------------
# 2. Two-attribute route (time, transfers)
# ---------------------------------------------------------

print("Problem 2 – Two-attribute route")

routes = [("A", 18, 0), ("B", 14, 1), ("C", 12, 2), ("D", 16, 0)]
# (name, time, transfers)

def route_score(t, k):
    return -t - 4 * k   # time penalty + transfer penalty

best_name = None
best_s = -float("inf")

for name, t, k in routes:
    s = route_score(t, k)
    print("Route", name, "score =", s)
    if s > best_s:
        best_s = s
        best_name = name

print("Best route:", best_name, "with score", best_s)
print()


# ---------------------------------------------------------
# 3. Snack tradeoff: fun vs. weight
# ---------------------------------------------------------

print("Problem 3 – Snack tradeoff")

snacks = [
    ("chips", 7, 2.0),   # (name, fun, weight)
    ("apple", 5, 0.4),
    ("cookie", 6, 0.8),
    ("soda", 4, 1.0),
]

def snack_score(fun, w):
    return fun - 0.75 * w

best_snack = None
best_s = -float("inf")

for name, fun, w in snacks:
    s = snack_score(fun, w)
    print(name, "score =", s)
    if s > best_s:
        best_s = s
        best_snack = name

print("Best snack:", best_snack, "with score", best_s)
print()


# ---------------------------------------------------------
# 4. Filter then best – classroom chores
# ---------------------------------------------------------

print("Problem 4 – Filter then best (chores)")

chores = [("trash", 3), ("wipe", 2), ("sweep", 5), ("boards", 1)]
time_limit = 3

best_chore = None
best_time = -1   # we want the most time-consuming chore we can still finish

for name, minutes in chores:
    if minutes <= time_limit and minutes > best_time:
        best_time = minutes
        best_chore = name

if best_chore is None:
    print("No chore fits in the time limit.")
else:
    print("Do:", best_chore, "which takes", best_time, "minutes")
print()


# ---------------------------------------------------------
# 5. Challenge – general selector best_choice
# ---------------------------------------------------------

print("Problem 5 – General selector best_choice")

def best_choice(options, score_fn):
    """
    options: list of items
    score_fn: function that takes an item and returns a numeric score
    Returns the item with the highest score.
    """
    best_item = None
    best_s = -float("inf")

    for opt in options:
        s = score_fn(opt)
        if s > best_s:
            best_s = s
            best_item = opt

    return best_item


# Test 1: routes with (time, transfers)
routes = [("A", 18, 0), ("B", 14, 1), ("C", 12, 2), ("D", 16, 0)]

def route_score_item(route):
    name, t, k = route
    return -t - 4 * k

best_route = best_choice(routes, route_score_item)
print("Best route (via best_choice):", best_route)

# Test 2: snacks with (price, fun)
snacks = [
    ("chips", 2.0, 7),   # (name, price, fun)
    ("apple", 1.0, 5),
    ("cookie", 1.5, 6),
]

budget = 2.0

def snack_score_item(snack):
    name, price, fun = snack
    if price > budget:
        return -float("inf")   # infeasible
    return fun

best_snack = best_choice(snacks, snack_score_item)
print("Best snack (via best_choice):", best_snack)
print()
