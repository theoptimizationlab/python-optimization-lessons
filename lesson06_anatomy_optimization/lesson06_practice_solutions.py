"""
Lesson 6 – Practice Problem Solutions
Formulations for the "From Words to Math" exercises.
"""

# ---------------------------------------------------------
# Problem 1 – Clothes shopping
# ---------------------------------------------------------
clothes_formulation = """
Problem 1 – Clothes shopping

Let:
  x = number of shirts
  y = number of pants

Objective (maximize style points):
  maximize  2x + 4y

Budget constraint:
  15x + 25y <= 100

Nonnegativity:
  x >= 0
  y >= 0
"""

print(clothes_formulation)
print("-" * 50)


# ---------------------------------------------------------
# Problem 2 – Shipping boxes
# ---------------------------------------------------------
shipping_formulation = """
Problem 2 – Shipping boxes

Let:
  x = number of boxes shipped by truck
  y = number of boxes shipped by train

Objective (minimize total shipping cost):
  minimize  5x + 3y

Constraints:
  x + y >= 40       (must ship at least 40 boxes)
  x >= 0
  y >= 0
"""

print(shipping_formulation)
print("-" * 50)


# ---------------------------------------------------------
# Problem 3 – Study planning
# ---------------------------------------------------------
study_formulation = """
Problem 3 – Study planning

Let:
  x = hours of math study
  y = hours of science study

Objective (maximize points):
  maximize  3x + 2y

Time constraint:
  x + y <= 10       (at most 10 hours available)

Nonnegativity:
  x >= 0
  y >= 0
"""

print(study_formulation)
print("-" * 50)
