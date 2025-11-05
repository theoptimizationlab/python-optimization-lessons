# Lesson 7 – Solving Optimization with SciPy (linprog)

**Goal**  
Use `scipy.optimize.linprog` to solve small linear optimization problems that we already know how to model.

### Key Ideas
- SciPy (`scipy.optimize.linprog`) can solve linear programs once we give:
  - `c` – coefficients of the objective  
  - `A_ub`, `b_ub` – matrix and vector for `<=` constraints  
  - `bounds` – lower/upper bounds for each variable  
- `linprog` always **minimizes**, so to solve a **maximize** problem we:
  - multiply the objective coefficients by `-1`  
  - after solving, multiply the reported objective value by `-1` again  
- To handle `>=` constraints, multiply the whole inequality by `-1` to turn it into `<=`.

### Files
- `lesson07_scipy_linprog.py` — examples with the bakery and transportation problems  
- `lesson07_practice_solutions.py` — SciPy code for the three practice problems (snack mix, study hours, toy factory)  

### Running
In Google Colab:
- SciPy is already installed.
- Just run the cells (or the script) after `from scipy.optimize import linprog`.

On a local machine:
- Install once with `pip install scipy`.
