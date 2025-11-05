"""
Lesson 7 – Practice Problem Solutions

Each problem:
- Models the variables, objective, and constraints
- Translates them into (c, A_ub, b_ub, bounds)
- Solves using scipy.optimize.linprog
"""

from scipy.optimize import linprog


def show_result(name, res, is_max=False):
    print("=== ", name, " ===")
    if not res.success:
        print("No optimal solution found.")
        print("Message:", res.message)
        print()
        return

    x = res.x
    value = -res.fun if is_max else res.fun

    print("x:", x)
    if is_max:
        print("Objective value (max):", value)
    else:
        print("Objective value (min):", value)
    print()


# ---------------------------------------------------------
# Problem 1 – Snack Mix (maximize)
# ---------------------------------------------------------
# Variables: x1 = units of nuts, x2 = units of raisins
# Objective: maximize 1 x1 + 2 x2
# Constraint: x1 + 2 x2 <= 8
# Bounds: x1, x2 >= 0
#
# For linprog (minimization), use objective: -x1 - 2 x2

def solve_snack_mix():
    c = [-1, -2]  # negate for maximization

    A_ub = [[1, 2]]
    b_ub = [8]

    bounds = [(0, None), (0, None)]

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")
    show_result("Problem 1 – Snack Mix (max)", res, is_max=True)


# ---------------------------------------------------------
# Problem 2 – Study Hours (maximize)
# ---------------------------------------------------------
# Variables: x1 = hours on Subject 1, x2 = hours on Subject 2
# Objective: maximize 4 x1 + 3 x2
# Constraint: x1 + x2 <= 10
# Bounds: x1, x2 >= 0

def solve_study_hours():
    c = [-4, -3]  # negate for maximization

    A_ub = [[1, 1]]
    b_ub = [10]

    bounds = [(0, None), (0, None)]

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")
    show_result("Problem 2 – Study Hours (max)", res, is_max=True)


# ---------------------------------------------------------
# Problem 3 – Toy Factory (maximize)
# ---------------------------------------------------------
# Variables: x1 = Toy A, x2 = Toy B
# Objective: maximize 5 x1 + 7 x2
# Constraints:
#   3 x1 + 4 x2 <= 60
#   x1 + x2     <= 20
# Bounds: x1, x2 >= 0

def solve_toy_factory():
    c = [-5, -7]  # negate for maximization

    A_ub = [
        [3, 4],
        [1, 1]
    ]
    b_ub = [60, 20]

    bounds = [(0, None), (0, None)]

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")
    show_result("Problem 3 – Toy Factory (max)", res, is_max=True)


# ---------------------------------------------------------
# Run all three practice problems
# ---------------------------------------------------------

if __name__ == "__main__":
    solve_snack_mix()
    solve_study_hours()
    solve_toy_factory()
