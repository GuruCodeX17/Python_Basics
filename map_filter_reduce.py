# ==========================================
# PYTHON MAP, FILTER & REDUCE
# COMPLETE EXAMPLES
# ==========================================


# ==========================================
# 1. map() - Transform every item
# ==========================================

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("Original numbers:", numbers)
print("Squares:", squares)


# ==========================================
# 2. map() - Double every number
# ==========================================

doubled = list(map(lambda x: x * 2, numbers))

print("\nDoubled numbers:", doubled)


# ==========================================
# 3. map() - Add a value to every number
# ==========================================

marks = [60, 70, 80, 90]

updated_marks = list(map(lambda mark: mark + 5, marks))

print("\nOriginal marks:", marks)
print("Updated marks:", updated_marks)


# ==========================================
# 4. map() - Convert strings to uppercase
# ==========================================

names = ["guru", "arun", "kumar", "priya"]

uppercase_names = list(map(lambda name: name.upper(), names))

print("\nOriginal names:", names)
print("Uppercase names:", uppercase_names)


# ==========================================
# 5. map() with a normal function
# ==========================================

def cube(number):
    return number ** 3


cubes = list(map(cube, numbers))

print("\nCubes:", cubes)


# ==========================================
# 6. filter() - Select even numbers
# ==========================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print("\nNumbers:", numbers)
print("Even numbers:", even_numbers)


# ==========================================
# 7. filter() - Select odd numbers
# ==========================================

odd_numbers = list(
    filter(lambda x: x % 2 != 0, numbers)
)

print("Odd numbers:", odd_numbers)


# ==========================================
# 8. filter() - Select numbers greater than 5
# ==========================================

greater_than_five = list(
    filter(lambda x: x > 5, numbers)
)

print("Numbers greater than 5:", greater_than_five)


# ==========================================
# 9. filter() with strings
# ==========================================

names = ["Guru", "Arun", "Kumar", "Priya", "Raj"]

long_names = list(
    filter(lambda name: len(name) > 4, names)
)

print("\nNames:", names)
print("Names with more than 4 characters:", long_names)


# ==========================================
# 10. filter() with marks
# ==========================================

marks = [35, 45, 55, 65, 75, 85, 95]

passed_marks = list(
    filter(lambda mark: mark >= 50, marks)
)

print("\nMarks:", marks)
print("Passed marks:", passed_marks)


# ==========================================
# 11. reduce() - Add all numbers
# ==========================================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(
    lambda a, b: a + b,
    numbers
)

print("\nNumbers:", numbers)
print("Total:", total)


# ==========================================
# 12. reduce() - Multiply all numbers
# ==========================================

product = reduce(
    lambda a, b: a * b,
    numbers
)

print("Product:", product)


# ==========================================
# 13. reduce() - Find the largest number
# ==========================================

numbers = [10, 25, 5, 40, 15]

largest = reduce(
    lambda a, b: a if a > b else b,
    numbers
)

print("\nNumbers:", numbers)
print("Largest number:", largest)


# ==========================================
# 14. reduce() - Find the smallest number
# ==========================================

smallest = reduce(
    lambda a, b: a if a < b else b,
    numbers
)

print("Smallest number:", smallest)


# ==========================================
# 15. map() + filter()
# ==========================================

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

squared_even_numbers = list(
    map(lambda x: x * x, even_numbers)
)

print("\nOriginal numbers:", numbers)
print("Even numbers:", even_numbers)
print("Squared even numbers:", squared_even_numbers)


# ==========================================
# 16. map() + filter() + reduce()
# ==========================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

squared_numbers = list(
    map(lambda x: x * x, even_numbers)
)

total = reduce(
    lambda a, b: a + b,
    squared_numbers
)

print("\nOriginal numbers:", numbers)
print("Even numbers:", even_numbers)
print("Squared numbers:", squared_numbers)
print("Sum of squared numbers:", total)


# ==========================================
# 17. Practical student example
# ==========================================

marks = [45, 67, 82, 39, 91, 76, 55]

# Add 5 bonus marks
bonus_marks = list(
    map(lambda mark: mark + 5, marks)
)

# Keep marks greater than or equal to 50
passed_marks = list(
    filter(lambda mark: mark >= 50, bonus_marks)
)

# Calculate total
total_marks = reduce(
    lambda a, b: a + b,
    passed_marks
)

print("\n--- Student Example ---")
print("Original marks:", marks)
print("Marks after bonus:", bonus_marks)
print("Passed marks:", passed_marks)
print("Total of passed marks:", total_marks)


# ==========================================
# 18. Practical AI/ML-style example
# ==========================================

features = [10, 20, 30, 40, 50]

# Simple transformation
scaled_features = list(
    map(lambda x: x / 10, features)
)

print("\n--- Feature Processing Example ---")
print("Original features:", features)
print("Transformed features:", scaled_features)


# ==========================================
# FINAL MESSAGE
# ==========================================

print("\n==========================================")
print("Map, Filter & Reduce Demo Completed!")
print("==========================================")