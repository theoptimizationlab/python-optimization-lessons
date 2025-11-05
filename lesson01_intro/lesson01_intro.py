"""
Lesson 1 – Introduction to Python and Optimization

Overview:
- Understand what variables are
- Practice math operations in Python
- Explore a simple optimization example

Optimization is about making the best possible choice under given limits.
This short script uses a fun example (buying candies) to show how Python can
help solve simple decision problems.
"""

# ---------------------------------------------------------
# 1. Variables – containers that store information
# ---------------------------------------------------------

apples = 5
bananas = 3
total_fruits = apples + bananas

print("=== Fruit Example ===")
print("Apples:", apples)
print("Bananas:", bananas)
print("Total fruits:", total_fruits)
print()  # blank line for readability


# ---------------------------------------------------------
# 2. Numbers and text (strings)
# ---------------------------------------------------------

name = "Jordan"
age = 16

print("=== Name and Age Example ===")
print("Hello", name)
print("You are", age, "years old.")
print()


# ---------------------------------------------------------
# 3. Basic math operations in Python
# ---------------------------------------------------------

a = 12
b = 5

print("=== Math Operations ===")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)     # normal division
print("a // b =", a // b)   # floor division (rounds down)
print("a % b =", a % b)     # remainder
print("a ** 2 =", a ** 2)   # exponent
print()


# ---------------------------------------------------------
# 4. Mini optimization example – buying candies
# ---------------------------------------------------------

money = 10      # total money available
price = 3       # cost per candy

candies = money // price  # how many full candies can you buy?

print("=== Optimization Example: Candy Buying ===")
print("Money available: $", money)
print("Price per candy: $", price)
print("Maximum candies you can buy:", candies)
print()


# ---------------------------------------------------------
# 5. Practice ideas
# ---------------------------------------------------------
# Try modifying this file or running small experiments:
#
# 1. Change the number of apples and bananas.
# 2. Use your own name in the greeting.
# 3. If you have $20 and a game costs $7,
#    how many games can you buy?
# 4. Compute the total cost of 3 notebooks at $2.50 each
#    including 6% tax.
#
# Save and run to see how Python responds!
