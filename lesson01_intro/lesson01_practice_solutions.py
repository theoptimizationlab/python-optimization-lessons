"""
Lesson 1 – Practice Problem Solutions

This file contains example solutions to the Lesson 1 practice problems.
Students are encouraged to try the problems on their own first before
looking at this file.
"""

# ---------------------------------------------------------
# Problem 1 – Favorite snacks total
# ---------------------------------------------------------
# Example: You have some cookies and some chips.
# Compute the total number of snacks.

cookies = 4
chips = 6
total = cookies + chips

print("Problem 1 – Favorite snacks total")
print("Total snacks:", total)
print()  # blank line


# ---------------------------------------------------------
# Problem 2 – Greeting with your name
# ---------------------------------------------------------
# Store a name in a variable and print a greeting.

name = "Alex"
print("Problem 2 – Greeting")
print("Hello,", name)
print()


# ---------------------------------------------------------
# Problem 3 – Buying video games
# ---------------------------------------------------------
# You have $20 and each video game costs $7.
# How many full games can you buy?

money = 20
price = 7
games = money // price  # integer (floor) division

print("Problem 3 – Video games")
print("You can buy", games, "games")
print()


# ---------------------------------------------------------
# Problem 4 – Total cost of notebooks with tax
# ---------------------------------------------------------
# Each notebook costs $2.50 and you buy 3.
# Sales tax is 6%. What is the total cost?

price_per_notebook = 2.50
quantity = 3
subtotal = price_per_notebook * quantity
tax_rate = 0.06

total = subtotal * (1 + tax_rate)

print("Problem 4 – Notebooks with tax")
print("Total cost:", total)
print()
