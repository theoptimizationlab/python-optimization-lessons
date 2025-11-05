"""
Lesson 4 – Data Structures: Organizing Options

In this lesson:
- Use lists to store ordered options
- Use tuples to group attributes (like time, fun)
- Use dictionaries to map names to values
- Combine data structures with loops to search for the best option
"""

# ---------------------------------------------------------
# 1. Lists – ordered collections
# ---------------------------------------------------------

print("=== Lists: Route Times ===")
times = [18, 13, 16, 11]

print("All times:", times)
print("First element:", times[0])
print("Last element:", times[-1])
print()

print("Loop over times:")
for t in times:
    print("Route takes", t, "minutes")
print()


# ---------------------------------------------------------
# 2. Tuples – grouping related values
# ---------------------------------------------------------

print("=== Tuples: Routes with Time and Fun ===")
routes = [(12, 8), (15, 10), (9, 6)]

for r in routes:
    print("Time:", r[0], "Fun:", r[1])
print()

# Find route with best fun
best_fun = -float("inf")
best_route = None

for time, fun in routes:
    if fun > best_fun:
        best_fun = fun
        best_route = (time, fun)

print("Route with best fun:", best_route)
print()


# ---------------------------------------------------------
# 3. Dictionaries – naming options
# ---------------------------------------------------------

print("=== Dictionaries: Snack Prices ===")
prices = {"apple": 2, "banana": 1, "chips": 3}

print("Price of apple:", prices["apple"])
print("Price of chips:", prices["chips"])
print()

print("Loop over dictionary:")
for snack, cost in prices.items():
    print(snack, "costs", cost)
print()


# ---------------------------------------------------------
# 4. Optimization connection – cheapest snack
# ---------------------------------------------------------

cheapest_item = None
cheapest_price = float("inf")

for snack, cost in prices.items():
    if cost < cheapest_price:
        cheapest_price = cost
        cheapest_item = snack

print("Cheapest snack:", cheapest_item, "at", cheapest_price)
print()

# ---------------------------------------------------------
# 5. Optimization connection – best affordable item by fun
# ---------------------------------------------------------

items = {
    "board game": (10, 7),   # (price, fun)
    "book": (8, 6),
    "video game": (15, 10)
}
budget = 12

best_item = None
best_fun = -float("inf")

for name, (price, fun) in items.items():
    if price <= budget and fun > best_fun:
        best_fun = fun
        best_item = name

print("Best item within budget:", best_item, "with fun =", best_fun)
