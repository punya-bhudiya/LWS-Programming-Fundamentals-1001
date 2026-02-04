"""
LWS – Programming Fundamentals 1001
Module: How Python Works

Author: Punya Bhudiya
Tutor at LearnWithStriver (LWS)

Purpose:
This file explains how Python executes code internally.
Understanding this helps with debugging and learning.
"""

# ==================================================
# STEP 1: WRITING PYTHON CODE
# ==================================================
# Python programs are written in files
# with the .py extension.

# Example:
# my_program.py

# ==================================================
# STEP 2: PYTHON INTERPRETER
# ==================================================
# Python uses an interpreter, not a compiler.

# Interpreter:
# - Reads code line by line
# - Executes immediately
# - Stops execution if an error occurs

# ==================================================
# STEP 3: INTERNAL EXECUTION FLOW
# ==================================================
# Python execution process:
# 1. Source code (.py)
# 2. Converted to bytecode
# 3. Executed by Python Virtual Machine (PVM)

# Learners do NOT need to manage this manually.
# Python handles it internally.

# ==================================================
# LINE-BY-LINE EXECUTION
# ==================================================
# Python executes code from top to bottom.

print("This line is executed first")

# Uncommenting the next line will cause an error
# print(undefined_variable)

print("This line executes only if no error occurs above")

# ==================================================
# ERROR HANDLING (INTRODUCTION)
# ==================================================
# If Python encounters an error:
# - Execution stops
# - Error message is displayed
# - Remaining code is not executed

# Errors are NOT failures.
# They are part of the learning process.

# ==================================================
# DEBUGGING
# ==================================================
# Debugging means finding and fixing errors.
# Understanding how Python works helps debug faster.

# ==================================================
# END OF FILE
# ==================================================
