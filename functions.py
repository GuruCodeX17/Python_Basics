# ===========================================
# PYTHON FUNCTIONS - ALL CONCEPTS
# ===========================================

print("========== PYTHON FUNCTIONS ==========\n")

# -------------------------------------------
# 1. Simple Function
# -------------------------------------------

def welcome():
    print("Welcome to Python Functions!")

welcome()

# -------------------------------------------
# 2. Function with Parameters
# -------------------------------------------

def greet(name):
    print("Hello,", name)

greet("Guru")

# -------------------------------------------
# 3. Function with Two Parameters
# -------------------------------------------

def add(a, b):
    print("Addition =", a + b)

add(10, 20)

# -------------------------------------------
# 4. Function with Return Value
# -------------------------------------------

def multiply(a, b):
    return a * b

result = multiply(5, 6)
print("Multiplication =", result)

# -------------------------------------------
# 5. Function with Default Parameter
# -------------------------------------------

def country(name="India"):
    print("Country:", name)

country()
country("Japan")

# -------------------------------------------
# 6. Function with Keyword Arguments
# -------------------------------------------

def student(name, age):
    print("Name:", name)
    print("Age :", age)

student(age=21, name="Guru")

# -------------------------------------------
# 7. Function with Variable Arguments (*args)
# -------------------------------------------

def total_marks(*marks):
    print("Marks:", marks)
    print("Total:", sum(marks))

total_marks(85, 90, 95, 88)

# -------------------------------------------
# 8. Function with Multiple Return Values
# -------------------------------------------

def calculation(a, b):
    return a+b, a-b, a*b

add_result, sub_result, mul_result = calculation(20, 10)

print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)

# -------------------------------------------
# 9. Recursive Function
# -------------------------------------------

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print("Factorial of 5 =", factorial(5))

# -------------------------------------------
# 10. Lambda Function
# -------------------------------------------

square = lambda x: x*x

print("Square of 8 =", square(8))

print("\n========== END OF PROGRAM ==========")