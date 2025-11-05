"""
Lesson 6 – Anatomy of an Optimization Problem

Key pieces:
- Decision variables
- Objective function
- Constraints
- Feasible region

Big idea:
Choose values for the decision variables that satisfy all constraints and make
the objective function as good as possible.
"""


# ---------------------------------------------------------
# 1. General structure – just as a template
# ---------------------------------------------------------

def describe_optimization_problem():
    """
    This function just prints the generic pieces of an optimization model.
    """
    print("An optimization problem has:")
    print("- Decision variables: what we control")
    print("- Objective function: what we want to maximize or minimize")
    print("- Constraints: rules and limits")
    print("- Feasible region: all choices that satisfy every constraint")
    print()


describe_optimization_problem()


# ---------------------------------------------------------
# 2. Example 1 – Snacks on a budget
#    From words -> math (formulation only)
# ---------------------------------------------------------

snacks_example = {
    "description": "Snacks on a $20 budget with apples and bananas.",
    "decision_variables": "x = apples, y = bananas",
    "objective": "maximize 2x + 3y   (fun points)",
    "constraints": [
        "3x + 2y <= 20   (budget)",
        "x >= 0",
        "y >= 0",
    ],
}

print("=== Example 1: Snacks on a Budget ===")
for k, v in snacks_example.items():
    print(f"{k}: {v}")
print()


# ---------------------------------------------------------
# 3. Example 2 – Travel routes (feasibility focus)
# ---------------------------------------------------------

routes = [
    {"name": "A", "time": 12, "cost": 2},
    {"name": "B", "time": 9,  "cost": 6},
    {"name": "C", "time": 10, "cost": 4},
]

time_limit = 10
cost_limit = 5

print("=== Example 2: Travel Routes (Feasibility) ===")
print("Time limit:", time_limit, "minutes")
print("Cost limit: $", cost_limit)

feasible_routes = []

for r in routes:
    feasible_time = r["time"] <= time_limit
    feasible_cost = r["cost"] <= cost_limit
    feasible = feasible_time and feasible_cost

    print(
        f"Route {r['name']}: time = {r['time']}, "
        f"cost = {r['cost']} -> feasible? {feasible}"
    )

    if feasible:
        feasible_routes.append(r["name"])

print("Feasible routes under both constraints:", feasible_routes)
print()
