"""
LWS – Programming Fundamentals 1001
Module: Modules

Author: Punya Bhudiya
Tutor at LearnWithStriver (LWS)

Purpose:
This file explains how Python modules help
organize and reuse code.
"""

# ==================================================
# WHAT IS A MODULE?
# ==================================================
# A module is a file containing Python code.
# It helps organize large programs.

# ==================================================
# IMPORTING BUILT-IN MODULES
# ==================================================

import math

print(math.sqrt(16))
print(math.pi)

# ==================================================
# IMPORTING SPECIFIC FUNCTIONS
# ==================================================

from math import pow

print(pow(2, 3))

# ==================================================
# RENAMING MODULES
# ==================================================

import math as m

print(m.factorial(5))

# ==================================================
# WHY MODULES ARE IMPORTANT
# ==================================================
# - Better code organization
# - Reusability
# - Cleaner programs

# ==================================================
# END OF FILE
# ==================================================
