"""
Lesson 7 – Solving Optimization Problems with SciPy (linprog)

This lesson shows how to:
- Translate a linear optimization model into Python lists and arrays
- Use scipy.optimize.linprog to solve it
- Handle maximization by negating the objective
- Handle >= constraints by multiplying both sides by -1
"""

from scipy.optimize import linprog


# ---------------------------------------------------------
# 1. Helper: print solution nicely
# ---------------------------------------------------------

def show_result(description, res, is_max=False):
    """
    description : short text about the problem
    res         : result object from linprog
    is_max      : True if we negated the objective (max problem)
    """
    print("=== ", description, " ===")
    if not res.success:
        print("Solver did not find an optimal solution.")
        print("Message:", res.message)
        print()
        return

    x = res.x
    value = -res.fun if is_max else res.fun

    print("Optimal x:", x)
    if is_max:
        print("Optimal objective (max):", value)
    else:
        print("Optimal objective (min):", value)
    print()


# ---------------------------------------------------------
# 2. Example 1 – Bakery problem (maximize profit)
# ---------------------------------------------------------
# Model (from the lesson notes):
# Variables: x1 = loaves of bread, x2 = cakes
# Maximize:  2 x1 + 5 x2
# Subject to: 2 x1 + 4 x2 <= 40
#            x1, x2 >= 0
#
# linprog always MINIMIZES, so we minimize: -2 x1 - 5 x2

def solve_bakery():
    # coefficients for - (2 x1 + 5 x2)
    c = [-2, -5]

    # inequality 2 x1 + 4 x2 <= 40
    A_ub = [[2, 4]]
    b_ub = [40]

    # bounds: x1 >= 0, x2 >= 0
    bounds = [(0, None), (0, None)]

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")
    show_result("Bakery problem (maximize profit)", res, is_max=True)


# ---------------------------------------------------------
# 3. Example 2 – Transportation (minimize cost)
# ---------------------------------------------------------
# Variables: x1 = truck shipments, x2 = train shipments
# Minimize: 3 x1 + 5 x2
# Constraint: x1 + x2 >= 10
# Bounds: x1, x2 >= 0
#
# To use <= form, multiply the constraint by -1:
#   x1 + x2 >= 10  ->  -x1 - x2 <= -10

def solve_transport():
    c = [3, 5]

    A_ub = [[-1, -1]]   # -x1 - x2 <= -10
    b_ub = [-10]

    bounds = [(0, None), (0, None)]

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")
    show_result("Transport problem (minimize cost)", res, is_max=False)


# ---------------------------------------------------------
# 4. Run all examples
# ---------------------------------------------------------

if __name__ == "__main__":
    solve_bakery()
    solve_transport()
    # Students can add more test cases here based on the practice set.
