# ==========================================
# PYTHON MODULES & PACKAGES - COMPLETE EXAMPLES
# ==========================================


# 1. Importing a built-in module

import math

print("Square root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Value of pi:", math.pi)


# 2. Using different functions from math

print("\nAbsolute value:", math.fabs(-10))
print("Ceiling:", math.ceil(4.2))
print("Floor:", math.floor(4.8))


# 3. Importing a specific function

from math import sqrt

print("\nSquare root using direct import:", sqrt(64))


# 4. Importing multiple functions

from math import factorial, gcd

print("Factorial of 5:", factorial(5))
print("GCD of 12 and 18:", gcd(12, 18))


# 5. Using an alias

import math as m

print("\nSquare root using alias:", m.sqrt(100))
print("Pi using alias:", m.pi)


# 6. Random module

import random

random_number = random.randint(1, 100)

print("\nRandom number:", random_number)


# 7. Selecting a random item

fruits = ["apple", "banana", "orange", "mango"]

random_fruit = random.choice(fruits)

print("Random fruit:", random_fruit)


# 8. Date and time module

import datetime

current_date = datetime.date.today()

print("\nCurrent date:", current_date)


current_time = datetime.datetime.now()

print("Current date and time:", current_time)


# 9. Creating your own module
#
# For this example, create another file:
#
# calculator.py
#
# Put this code inside calculator.py:
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     return a / b
#
# Then use:
#
# from calculator import add, subtract, multiply, divide
#
# print(add(10, 5))
# print(subtract(10, 5))
# print(multiply(10, 5))
# print(divide(10, 5))


# 10. Importing the complete custom module
#
# If calculator.py exists:
#
# import calculator
#
# print(calculator.add(10, 5))
# print(calculator.multiply(10, 5))


# 11. Using __name__

def welcome():
    print("\nWelcome to Python Modules!")


if __name__ == "__main__":
    welcome()


# 12. Creating a useful utility function

def calculate_square(number):
    return number * number


print("\nSquare of 7:", calculate_square(7))


# 13. Working with the os module

import os

print("\nCurrent directory:")
print(os.getcwd())


# 14. Listing files and folders

print("\nFiles and folders:")
print(os.listdir())


# 15. Checking whether a file exists

filename = "student.txt"

if os.path.exists(filename):
    print(f"\n{filename} exists.")
else:
    print(f"\n{filename} does not exist.")


# 16. Creating a simple package
#
# Example package structure:
#
# my_package/
#     __init__.py
#     calculator.py
#     converter.py
#
# You can then import:
#
# from my_package.calculator import add
#
# result = add(10, 20)
# print(result)


# 17. Practical example using modules

import statistics

marks = [80, 85, 90, 75, 95]

print("\nMarks:", marks)
print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))


print("\n===================================")
print("Modules and Packages Demo Complete!")
print("===================================")
# Using our custom calculator module

import calculator

print("\n--- Calculator Module ---")

print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))
print("Division:", calculator.divide(10, 5))