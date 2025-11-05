"""
Lesson 3 – Functions: Building Blocks for Optimization

In this lesson:
- Define and use functions
- Pass one or more inputs
- Combine functions with loops to test many options
"""

# ---------------------------------------------------------
# 1. Simple function example
# ---------------------------------------------------------

def greet(name):
    print("Hello,", name)

print("=== Greeting Example ===")
greet("Jordan")
greet("Maya")
print()

# ---------------------------------------------------------
# 2. Math function
# ---------------------------------------------------------

def square(x):
    return x * x

print("=== Square Example ===")
print(square(3))
print(square(5))
print()

# ---------------------------------------------------------
# 3. Function with two inputs
# ---------------------------------------------------------

def affordable(price, budget):
    if price <= budget:
        return True
    else:
        return False

print("=== Affordable Example ===")
print(affordable(5, 10))
print(affordable(12, 10))
print()

# ---------------------------------------------------------
# 4. Total cost
# ---------------------------------------------------------

def total_cost(quantity, unit_price):
    return quantity * unit_price

print("=== Total Cost Example ===")
print(total_cost(4, 3))
print(total_cost(2, 7))
print()

# ---------------------------------------------------------
# 5. Functions + loops
# ---------------------------------------------------------

def affordable(price, budget):
    return price <= budget

prices = [5, 3, 7, 2, 9]
budget = 6

print("=== Affordable Items ===")
for p in prices:
    if affordable(p, budget):
        print("You can buy item that costs:", p)
print()

# ---------------------------------------------------------
# 6. Scoring and optimization example
# ---------------------------------------------------------

def score(time, fun):
    return fun - 0.5 * time

routes = [(12, 8), (15, 10), (9, 6)]  # (time, fun)

best_score = -float('inf')
best_route = None

for time, fun in routes:
    s = score(time, fun)
    print("Route:", (time, fun), "score =", s)
    if s > best_score:
        best_score = s
        best_route = (time, fun)

print()
print("Best route:", best_route, "with score =", best_score)
