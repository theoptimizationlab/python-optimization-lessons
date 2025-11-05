"""
Lesson 4 – Practice Problem Solutions
"""

# ---------------------------------------------------------
# 1. Largest number in a list
# ---------------------------------------------------------

print("Problem 1 – Largest number")

nums = [12, 7, 25, 9, 18]

largest = -float('inf')
for n in nums:
    if n > largest:
        largest = n

print("Largest number is:", largest)
print()  # blank line


# ---------------------------------------------------------
# 2. Prices under budget
# ---------------------------------------------------------

print("Problem 2 – Prices under budget")

prices = [12, 8, 5]
budget = 10

for p in prices:
    if p < budget:
        print("Affordable:", p)
print()


# ---------------------------------------------------------
# 3. Best route by fun
# ---------------------------------------------------------

print("Problem 3 – Best route by fun")

routes = [(12, 8), (15, 10), (9, 6)]
best_fun = -float('inf')
best_route = None

for t, f in routes:
    if f > best_fun:
        best_fun = f
        best_route = (t, f)

print("Best route by fun:", best_route)
print()


# ---------------------------------------------------------
# 4. Cheapest snack from dictionary
# ---------------------------------------------------------

print("Problem 4 – Cheapest snack")

snacks = {"apple": 2, "banana": 1, "chips": 3}
cheapest_item = None
cheapest_price = float('inf')

for snack, price in snacks.items():
    if price < cheapest_price:
        cheapest_price = price
        cheapest_item = snack

print("Cheapest snack:", cheapest_item, "at", cheapest_price)
print()


# ---------------------------------------------------------
# 5. Challenge – most fun item within budget
# ---------------------------------------------------------

print("Problem 5 – Best item within budget by fun")

items = {
    "board game": (10, 7),
    "book": (8, 6),
    "video game": (15, 10)
}
budget = 12
best_item = None
best_fun = -float('inf')

for name, (price, fun) in items.items():
    if price <= budget and fun > best_fun:
        best_fun = fun
        best_item = name

print("Best item within budget:", best_item, "with fun =", best_fun)
