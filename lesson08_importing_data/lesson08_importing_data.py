"""
Lesson 8 – Importing Data and Optimizing with Python

We use:
- pandas to read an Excel spreadsheet (smoothies.xlsx)
- numpy to build arrays for the solver
- scipy.optimize.linprog to solve a linear program
- matplotlib to visualize the optimal smoothie mix

Model (Smoothie Stand):

Variables:
  xA, xB, xC, xD, xE = cups of each recipe to make (A..E, in that order)

Objective:
  maximize sum_j profit_per_cup[j] * x_j

Constraints:
  sum_j fruit_cups[j]   * x_j  <= 60
  sum_j yogurt_cups[j]  * x_j  <= 30
  sum_j ice_cups[j]     * x_j  <= 70
  sum_j vitaminC_mg[j]  * x_j  >= 1800

Bounds:
  x_j >= 0  for all j

Note:
  linprog minimizes, so we negate the profit coefficients.
  The vitamin C >= constraint is turned into <= by multiplying by -1.
"""

import pandas as pd
import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt


def build_model_from_excel(filename="smoothies.xlsx", sheet="recipes"):
    """
    Reads smoothie data from an Excel file and builds:
      - names: list of recipe names
      - c: objective coefficients (negated for maximization)
      - A_ub, b_ub: inequality constraints in A_ub x <= b_ub form
      - bounds: nonnegativity bounds for each variable
    """

    # Step 1: read the sheet into a DataFrame
    recipes = pd.read_excel(filename, sheet_name=sheet)

    # We expect columns:
    # recipe, profit_per_cup, fruit_cups, yogurt_cups, ice_cups, vitaminC_mg
    print("Data preview:")
    print(recipes.head())
    print()

    # Keep the recipe names in order to label variables and plots later
    names = recipes["recipe"].tolist()
    print("Variable order:", names)

    # Step 3: map columns to arrays

    # Objective: maximize profit => minimize negative profit
    c = -recipes["profit_per_cup"].to_numpy()  # shape: (n_vars,)

    # Resource constraints (fruit, yogurt, ice)  => A_resources x <= b_resources
    A_resources = recipes[["fruit_cups", "yogurt_cups", "ice_cups"]].to_numpy().T
    b_resources = np.array([60.0, 30.0, 70.0])

    # Vitamin C minimum: sum vitaminC_mg[j] * x_j >= 1800
    # Multiply by -1 to convert to <=
    vitamin_row = -recipes["vitaminC_mg"].to_numpy()
    A_ub = np.vstack([A_resources, vitamin_row])
    b_ub = np.concatenate([b_resources, np.array([-1800.0])])

    # Nonnegativity bounds: each x_j >= 0
    n = len(recipes)
    bounds = [(0, None)] * n

    print("Shapes:")
    print("  c:", c.shape)
    print("  A_ub:", A_ub.shape)
    print("  b_ub:", b_ub.shape)
    print()

    return names, c, A_ub, b_ub, bounds


def solve_smoothies():
    """
    Build the model from smoothies.xlsx and solve with linprog.
    """

    names, c, A_ub, b_ub, bounds = build_model_from_excel()

    # Step 4: solve with linprog
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

    print("Solver success:", res.success)
    print("Status:", res.message)

    if not res.success:
        return

    x = res.x
    max_profit = -res.fun  # flip sign back for maximization

    print("Optimal quantities (in order", names, "):")
    print(x)
    print("Maximum profit:", max_profit)
    print()

    # Step 5: visualize the solution
    plt.bar(names, x)
    plt.title("Optimal Smoothie Mix")
    plt.xlabel("Recipe")
    plt.ylabel("Cups to make")
    plt.tight_layout()
    plt.savefig("linprog-smoothies-bar-chart.png", dpi=200)
    plt.close()
    print("Saved bar chart to linprog-smoothies-bar-chart.png")


if __name__ == "__main__":
    solve_smoothies()
