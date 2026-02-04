"""
LWS – Programming Fundamentals 1001
Module: Variable Scope

Author: Punya Bhudiya
Tutor at LearnWithStriver (LWS)

Purpose:
This file explains local and global scope.
"""

# ==================================================
# GLOBAL VARIABLE
# ==================================================

x = 10

def show():
    print(x)

show()

# ==================================================
# LOCAL VARIABLE
# ==================================================

def display():
    y = 5
    print(y)

display()

# print(y)  # Error: y is local to display()

# ==================================================
# GLOBAL KEYWORD
# ==================================================

count = 0

def increment():
    global count
    count += 1

increment()
print(count)

# ==================================================
# KEY TAKEAWAYS
# ==================================================
# - Local variables exist inside functions
# - Global variables exist throughout the program
# - Use global keyword carefully

# ==================================================
# END OF FILE
# ==================================================
