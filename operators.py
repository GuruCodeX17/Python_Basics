# ==========================================
# Python Operators
# Author: Guru
# ==========================================

# Variables
a = 20
b = 10

print("===== Arithmetic Operators =====")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

print("\n===== Comparison Operators =====")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print("\n===== Logical Operators =====")

age = 20
has_id = True

print("Eligible for Driving License:", age >= 18 and has_id)
print("Eligible for Student Discount:", age < 25 or has_id)
print("Not Eligible:", not(age >= 18))