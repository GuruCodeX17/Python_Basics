# ============================================
# PYTHON TUPLES - COMPLETE PROGRAM
# ============================================

print("\n========== PYTHON TUPLES ==========\n")

# --------------------------------------------
# 1. Creating a Tuple
# --------------------------------------------
print("1. Creating a Tuple")

fruits = ("Apple", "Banana", "Mango", "Orange")
print(fruits)

# --------------------------------------------
# 2. Accessing Elements
# --------------------------------------------
print("\n2. Accessing Elements")

print("First Fruit :", fruits[0])
print("Third Fruit :", fruits[2])

# --------------------------------------------
# 3. Positive Indexing
# --------------------------------------------
print("\n3. Positive Indexing")

print(fruits[1])

# --------------------------------------------
# 4. Negative Indexing
# --------------------------------------------
print("\n4. Negative Indexing")

print(fruits[-1])

# --------------------------------------------
# 5. Tuple Slicing
# --------------------------------------------
print("\n5. Tuple Slicing")

numbers = (10, 20, 30, 40, 50, 60, 70)

print(numbers[1:5])
print(numbers[:4])
print(numbers[3:])
print(numbers[::-1])

# --------------------------------------------
# 6. Tuple Length
# --------------------------------------------
print("\n6. Length")

print(len(numbers))

# --------------------------------------------
# 7. Count
# --------------------------------------------
print("\n7. count()")

values = (10, 20, 10, 30, 10)

print(values.count(10))

# --------------------------------------------
# 8. Index
# --------------------------------------------
print("\n8. index()")

print(values.index(30))

# --------------------------------------------
# 9. Membership
# --------------------------------------------
print("\n9. Membership")

if 20 in values:
    print("20 Found")

if 50 not in values:
    print("50 Not Found")

# --------------------------------------------
# 10. Loop Through Tuple
# --------------------------------------------
print("\n10. Loop Through Tuple")

for item in fruits:
    print(item)

# --------------------------------------------
# 11. Nested Tuple
# --------------------------------------------
print("\n11. Nested Tuple")

students = (
    ("Guru", 21),
    ("Rahul", 22),
    ("Priya", 20)
)

print(students)
print(students[0])
print(students[1][0])

# --------------------------------------------
# 12. Tuple Concatenation
# --------------------------------------------
print("\n12. Concatenation")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)

# --------------------------------------------
# 13. Tuple Repetition
# --------------------------------------------
print("\n13. Repetition")

print(("Python",) * 3)

# --------------------------------------------
# 14. Convert Tuple to List
# --------------------------------------------
print("\n14. Tuple to List")

numbers = (1, 2, 3)

list_numbers = list(numbers)

print(list_numbers)

# --------------------------------------------
# 15. Convert List to Tuple
# --------------------------------------------
print("\n15. List to Tuple")

my_list = [10, 20, 30]

my_tuple = tuple(my_list)

print(my_tuple)

# --------------------------------------------
# 16. Maximum, Minimum, Sum
# --------------------------------------------
print("\n16. max(), min(), sum()")

marks = (85, 90, 78, 88, 95)

print("Maximum :", max(marks))
print("Minimum :", min(marks))
print("Sum :", sum(marks))

# --------------------------------------------
# 17. Real World Example
# --------------------------------------------
print("\n17. Student Details")

student = ("Guru", "CSE", 8.15)

print("Name :", student[0])
print("Department :", student[1])
print("CGPA :", student[2])

print("\n========== END OF PROGRAM ==========")