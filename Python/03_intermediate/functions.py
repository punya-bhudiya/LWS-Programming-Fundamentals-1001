"""
LWS – Programming Fundamentals 1001
Module: Functions

Author: Punya Bhudiya
Tutor at LearnWithStriver (LWS)

Purpose:
This file explains functions and code reusability.
"""

# ==================================================
# WHAT IS A FUNCTION?
# ==================================================
# A function is a block of reusable code
# designed to perform a specific task.

# ==================================================
# DEFINING A FUNCTION
# ==================================================

def greet():
    print("Hello, welcome to LWS")

greet()

# ==================================================
# FUNCTION WITH PARAMETERS
# ==================================================

def greet_user(name):
    print("Hello", name)

greet_user("Punya")

# ==================================================
# FUNCTION WITH RETURN VALUE
# ==================================================

def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)

# ==================================================
# DEFAULT PARAMETERS
# ==================================================

def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(2, 3))

# ==================================================
# KEY TAKEAWAYS
# ==================================================
# - Functions improve reusability
# - Parameters pass data
# - return sends result back

# ==================================================
# END OF FILE
# ==================================================
