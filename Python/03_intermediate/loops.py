"""
LWS – Programming Fundamentals 1001
Module: Loops

Author: Punya Bhudiya
Tutor at LearnWithStriver (LWS)

Purpose:
This file explains repetition using loops in Python.
"""

# ==================================================
# WHAT ARE LOOPS?
# ==================================================
# Loops allow repeated execution of code
# until a condition is met.

# ==================================================
# FOR LOOP
# ==================================================

for i in range(5):
    print("Iteration:", i)

# ==================================================
# WHILE LOOP
# ==================================================

count = 1

while count <= 5:
    print("Count:", count)
    count += 1

# ==================================================
# BREAK STATEMENT
# ==================================================

for i in range(10):
    if i == 5:
        break
    print(i)

# ==================================================
# CONTINUE STATEMENT
# ==================================================

for i in range(5):
    if i == 2:
        continue
    print(i)

# ==================================================
# NESTED LOOPS
# ==================================================

for i in range(3):
    for j in range(2):
        print(i, j)

# ==================================================
# KEY TAKEAWAYS
# ==================================================
# - Loops reduce code duplication
# - for is used when range is known
# - while is used when condition-based

# ==================================================
# END OF FILE
# ==================================================
