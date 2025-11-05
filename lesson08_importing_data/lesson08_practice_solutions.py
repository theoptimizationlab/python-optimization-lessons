"""
Lesson 8 – Practice Problem Solutions

These examples reuse the smoothie model and show how to:
- Add a new recipe
- Tighten a resource limit
- Add upper bounds on certain decision variables
"""

import pandas as pd
import numpy as np
from scipy.optimize import linprog


def build_model_from_excel(filename="smoothies.xlsx", sheet="recipes",
                           fruit_limit=60.0, yogurt_limit=30.0,
                           ice_limit=70.0, vitC_min=1800.0,
                           bounds_override=None):
    """
    Generalized builder for the smoothie model.

    Parameters:
      fruit_limit, yogurt_limit, ice_limit : resource limits
      vitC_min                             : minimum vitamin C total
      bounds_override                      : if not None, use this list of bounds
                                              instead of the default (0, None)
    Returns:
      names, c, A_ub, b_ub, bounds
    """

    recipes = pd.read_excel(filename, sheet_name=sheet)
    names = recipes["recipe"].tolist()

    # Objective (maximize) -> negate for linprog
    c = -recipes["profit_per_cup"].to_numpy()

    # Resource constraints
    A_resources = recipes[["fruit_cups", "yogurt_cups", "ice_cups"]].to_numpy().T
    b_resources = np.array([fruit_limit, yogurt_limit, ice_limit])

    # Vitamin C >= vitC_min -> multiply by -1 to get <=
    vitamin_row = -recipes["vitaminC_mg"].to_numpy()
    A_ub = np.vstack([A_resources, vitamin_row])
    b_ub = np.concatenate([b_resources, np.array([-vitC_min])])

    n = len(recipes)

    if bounds_override is not None:
        bounds = bounds_override
    else:
        bounds = [(0, None)] * n

    return names, c, A_ub, b_ub, bounds


def solve_and_print(tag, *builder_args, **builder_kwargs):
    """
    Helper to build a model, solve it, and print the result.
    """

    names, c, A_ub, b_ub, bounds = build_model_from_excel(
        *builder_args, **builder_kwargs
    )

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

    print("=== ", tag, " ===")
    if not res.success:
        print("Solver failed:", res.message)
        print()
        return

    x = res.x
    max_profit = -res.fun

    print("Variable order:", names)
    print("Optimal quantities:", x)
    print("Maximum profit:", max_profit)
    print()


# ---------------------------------------------------------
# Practice 1 – Add a new recipe F
# ---------------------------------------------------------
# After editing the Excel file to add row F:
#   F, 1.9, 0.7, 0.4, 1.0, 45
# we can simply re-run the same model. The builder will
# automatically pick up the extra column because it reads
# all rows in the sheet. :contentReference[oaicite:5]{index=5}
def practice_1_add_recipe_F():
    solve_and_print("Practice 1 – With new recipe F")


# ---------------------------------------------------------
# Practice 2 – Tighten ice limit from 70 to 50
# ---------------------------------------------------------

def practice_2_tighter_ice():
    solve_and_print(
        "Practice 2 – Ice limit 50 instead of 70",
        ice_limit=50.0,
    )


# ---------------------------------------------------------
# Practice 3 – Demand caps A ≤ 15 and C ≤ 20
# ---------------------------------------------------------
# We assume recipes are ordered [A, B, C, D, E] in the sheet.
# Then bounds for variables (xA, xB, xC, xD, xE) can be:
#   (0, 15), (0, None), (0, 20), (0, None), (0, None)
# which enforces xA <= 15 and xC <= 20. :contentReference[oaicite:6]{index=6}

def practice_3_caps_on_A_and_C():
    # Load recipes just to know how many variables there are
    recipes = pd.read_excel("smoothies.xlsx", sheet_name="recipes")
    n = len(recipes)

    # Default: no upper bound
    bounds = [(0, None)] * n

    # Try to find indices for A and C based on the "recipe" column
    names = recipes["recipe"].tolist()
    # This is safer than assuming fixed positions
    idx_A = names.index("A") if "A" in names else None
    idx_C = names.index("C") if "C" in names else None

    if idx_A is not None:
        bounds[idx_A] = (0, 15)
    if idx_C is not None:
        bounds[idx_C] = (0, 20)

    solve_and_print(
        "Practice 3 – Caps on A and C",
        bounds_override=bounds,
    )


if __name__ == "__main__":
    # Run all three practice variations.
    # Make sure smoothies.xlsx is in the same folder, updated
    # according to each exercise description.
    practice_1_add_recipe_F()
    practice_2_tighter_ice()
    practice_3_caps_on_A_and_C()
