"""
LWS – Programming Fundamentals 1001
Module: Conditional Statements

Author: Punya Bhudiya
Tutor at LearnWithStriver (LWS)

Purpose:
This file explains decision-making in Python using
if, elif, and else statements.
"""

# ==================================================
# WHAT ARE CONDITIONAL STATEMENTS?
# ==================================================
# Conditional statements allow a program to make decisions.
# The program executes different code blocks
# based on conditions.

# ==================================================
# IF STATEMENT
# ==================================================

age = 18

if age >= 18:
    print("You are eligible to vote")

# ==================================================
# IF-ELSE STATEMENT
# ==================================================

number = 10

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ==================================================
# IF-ELIF-ELSE STATEMENT
# ==================================================

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# ==================================================
# NESTED CONDITIONS
# ==================================================

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Invalid user")

# ==================================================
# KEY TAKEAWAYS
# ==================================================
# - Conditions control program flow
# - Indentation is mandatory in Python
# - Conditions use comparison operators

# ==================================================
# END OF FILE
# ==================================================
