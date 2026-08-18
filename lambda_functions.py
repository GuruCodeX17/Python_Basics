# ==========================================
# PYTHON LAMBDA FUNCTIONS - COMPLETE EXAMPLES
# ==========================================


# 1. Basic lambda function

square = lambda x: x * x

print("Square of 5:", square(5))


# 2. Lambda with multiple arguments

add = lambda a, b: a + b

print("\nAddition:", add(10, 20))


# 3. Lambda for subtraction

subtract = lambda a, b: a - b

print("Subtraction:", subtract(20, 10))


# 4. Lambda for multiplication

multiply = lambda a, b: a * b

print("Multiplication:", multiply(10, 5))


# 5. Lambda for division

divide = lambda a, b: a / b

print("Division:", divide(20, 5))


# 6. Lambda with if-else

number = 10

check = lambda x: "Even" if x % 2 == 0 else "Odd"

print("\nNumber:", number)
print("Result:", check(number))


# 7. Lambda to find the largest number

maximum = lambda a, b: a if a > b else b

print("\nLargest number:", maximum(25, 40))


# 8. Lambda with a list

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("\nOriginal numbers:", numbers)
print("Squares:", squares)


# 9. Lambda with map()

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))

print("\nDoubled numbers:", doubled)


# 10. Lambda with filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print("\nEven numbers:", even_numbers)


# 11. Filter odd numbers

odd_numbers = list(
    filter(lambda x: x % 2 != 0, numbers)
)

print("Odd numbers:", odd_numbers)


# 12. Lambda with strings

names = ["Guru", "Arun", "Kumar", "Priya"]

long_names = list(
    filter(lambda name: len(name) > 4, names)
)

print("\nNames:", names)
print("Names with more than 4 characters:", long_names)


# 13. Lambda with sorted()

students = [
    ("Guru", 85),
    ("Arun", 92),
    ("Kumar", 78),
    ("Priya", 88)
]

students_sorted = sorted(
    students,
    key=lambda student: student[1]
)

print("\nStudents sorted by marks:")
for student in students_sorted:
    print(student)


# 14. Sorting in descending order

students_descending = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("\nStudents sorted by highest marks:")

for student in students_descending:
    print(student)


# 15. Lambda with dictionaries

employees = [
    {"name": "Guru", "salary": 50000},
    {"name": "Arun", "salary": 60000},
    {"name": "Kumar", "salary": 45000}
]

employees_sorted = sorted(
    employees,
    key=lambda employee: employee["salary"]
)

print("\nEmployees sorted by salary:")

for employee in employees_sorted:
    print(employee)


# 16. Lambda with map() and strings

names = ["guru", "arun", "kumar"]

uppercase_names = list(
    map(lambda name: name.upper(), names)
)

print("\nOriginal names:", names)
print("Uppercase names:", uppercase_names)


# 17. Lambda with map() and calculations

marks = [70, 80, 90, 60, 85]

bonus_marks = list(
    map(lambda mark: mark + 5, marks)
)

print("\nOriginal marks:", marks)
print("Marks after bonus:", bonus_marks)


# 18. Lambda with filter() and marks

passed_students = list(
    filter(lambda mark: mark >= 50, marks)
)

print("\nPassed marks:", passed_students)


# 19. Practical AI/ML-style example

features = [10, 20, 30, 40, 50]

scaled_features = list(
    map(lambda x: x / 10, features)
)

print("\nOriginal features:", features)
print("Scaled features:", scaled_features)


# 20. Practical final example

numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

squared_numbers = list(
    map(lambda x: x * x, even_numbers)
)

print("\nOriginal numbers:", numbers)
print("Even numbers:", even_numbers)
print("Squares of even numbers:", squared_numbers)


print("\n===================================")
print("Lambda Functions Demo Completed!")
print("===================================")