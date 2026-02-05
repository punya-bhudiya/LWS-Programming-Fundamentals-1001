"""
LWS – Programming Fundamentals 1001
Module: Type Casting

Author: Punya Bhudiya
Tutor at LearnWithStriver (LWS)
"""

# ==================================================
# WHAT IS TYPE CASTING?
# ==================================================
# Type casting means converting one data type
# into another.

# ==================================================
# STRING TO INTEGER
# ==================================================

age = "21"
age_int = int(age)

print(age_int)
print(type(age_int))

# ==================================================
# INTEGER TO STRING
# ==================================================

score = 95
score_str = str(score)

print(score_str)
print(type(score_str))

# ==================================================
# FLOAT CONVERSION
# ==================================================

value = "3.14"
float_value = float(value)

print(float_value)

# ==================================================
# COMMON ERRORS
# ==================================================
# int("abc")  # ValueError

# ==================================================
# END OF FILE
# ==================================================
