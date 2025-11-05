# Lesson 8 – Importing Data and Optimizing with Python

**Goal**  
Move from "hard-coded numbers" to reading data from a spreadsheet, then build and solve an optimization model in Python.

We use:
- **pandas** for reading an Excel sheet into a DataFrame  
- **numpy** for building vectors and matrices  
- **scipy.optimize.linprog** for solving the linear program  
- **matplotlib** for visualizing the optimal smoothie mix  

### Problem Setup – Smoothie Stand

We sell 5 smoothie recipes (A–E). Each recipe uses fruit, yogurt, and ice, and earns a profit per cup.  
We have limited supplies and must hit a minimum amount of vitamin C.

- Decision variables: cups of each recipe to make  
- Objective: maximize total profit  
- Constraints:
  - Fruit use ≤ 60 cups  
  - Yogurt use ≤ 30 cups  
  - Ice use ≤ 70 cups  
  - Total vitamin C ≥ 1800 mg  
  - All decision variables ≥ 0  

The data lives in an Excel file `smoothies.xlsx` with a sheet `"recipes"` and columns:

`recipe, profit_per_cup, fruit_cups, yogurt_cups, ice_cups, vitaminC_mg` :contentReference[oaicite:3]{index=3}  

### Files

- `lesson08_importing_data.py` — reads `smoothies.xlsx`, builds the model, solves with `linprog`, and saves a bar chart of the optimal mix  
- `lesson08_practice_solutions.py` — sample code for the Lesson 8 practice variations (add a recipe, tighten limits, add caps)  

### Requirements

On Google Colab:
- `pandas`, `numpy`, `scipy`, and `matplotlib` are usually already available.

On a local machine:
- Install once with:  
  `pip install pandas openpyxl scipy matplotlib`

Note: `read_excel` requires the **openpyxl** engine.
