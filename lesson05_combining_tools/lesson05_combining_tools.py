"""
Lesson 5 – Combining Conditions, Loops, and Functions

We now combine our three "superpowers":
- Conditions: enforce constraints (feasible or not)
- Loops: explore many options
- Functions: apply the same rule reliably to each option

Pattern:  Constraint → Evaluate → Keep Best
"""

# ---------------------------------------------------------
# Example 1 – Cheapest shopping within a budget
# ---------------------------------------------------------

print("=== Example 1: Cheapest Shopping Within a Budget ===")

prices = [12.5, 7.0, 9.5, 5.0, 14.0]
budget = 10.0

best_price = float("inf")   # start with an impossibly large value
best_idx = -1               # -1 means "no feasible item yet"

for i, p in enumerate(prices):
    # constraint: p <= budget
    # objective: make p as small as possible
    if p <= budget and p < best_price:
        best_price = p
        best_idx = i

if best_idx == -1:
    print("Nothing affordable.")
else:
    print("Cheapest within budget is item", best_idx, "at", best_price)

print()


# ---------------------------------------------------------
# Example 2 – Best route with time and transfers
# ---------------------------------------------------------

print("=== Example 2: Best Route with Time and Transfers ===")

routes = [("A", 18, 0), ("B", 14, 1), ("C", 12, 2), ("D", 16, 0)]
# route = (name, time_min, transfers)

def route_score(time_min, transfers):
    # Penalize both time and transfers.
    # Higher score is better (less time, fewer transfers).
    return -time_min - 5 * transfers

best_name = None
best_score = -float("inf")

for name, t, k in routes:
    s = route_score(t, k)
    print("Route", name, "has score", s)
    if s > best_score:
        best_score = s
        best_name = name

print("Best route is", best_name, "with score", best_score)
print()


# ---------------------------------------------------------
# Example 3 – Packing snacks (score = fun - 0.5 * weight)
# ---------------------------------------------------------

print("=== Example 3: Packing Snacks ===")

snacks = [
    ("chips", 7, 2.0),   # (name, fun, weight)
    ("apple", 5, 0.4),
    ("cookie", 6, 0.8),
    ("soda", 4, 1.0),
]

def snack_score(fun, weight):
    # reward fun, penalize weight
    return fun - 0.5 * weight

best = None
best_s = -float("inf")

for name, fun, wt in snacks:
    s = snack_score(fun, wt)
    print(name, "score =", s)
    if s > best_s:
        best_s = s
        best = name

print("Pick:", best, "with score", best_s)
print()

# Students can try variations:
# - Change the weight penalty to 1.0 or 0.25 and see which snack becomes best.
# - Change routes, prices, or budgets to see how the "best" option changes.
