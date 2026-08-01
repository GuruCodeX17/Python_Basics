# ============================================
# PYTHON LISTS - COMPLETE PROGRAM
# ============================================

print("\n========== PYTHON LISTS ==========\n")

# --------------------------------------------------
# 1. Creating a List
# --------------------------------------------------
print("1. Creating a List")

fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits)

# --------------------------------------------------
# 2. Accessing Elements
# --------------------------------------------------
print("\n2. Accessing Elements")

print("First Fruit :", fruits[0])
print("Third Fruit :", fruits[2])

# --------------------------------------------------
# 3. Positive Indexing
# --------------------------------------------------
print("\n3. Positive Indexing")

print(fruits[1])

# --------------------------------------------------
# 4. Negative Indexing
# --------------------------------------------------
print("\n4. Negative Indexing")

print(fruits[-1])

# --------------------------------------------------
# 5. List Slicing
# --------------------------------------------------
print("\n5. List Slicing")

numbers = [10,20,30,40,50,60,70]

print(numbers[1:5])
print(numbers[:4])
print(numbers[3:])
print(numbers[::-1])

# --------------------------------------------------
# 6. Updating List Elements
# --------------------------------------------------
print("\n6. Updating List")

numbers[2] = 300
print(numbers)

# --------------------------------------------------
# 7. Append()
# --------------------------------------------------
print("\n7. append()")

numbers.append(80)
print(numbers)

# --------------------------------------------------
# 8. Insert()
# --------------------------------------------------
print("\n8. insert()")

numbers.insert(2,25)
print(numbers)

# --------------------------------------------------
# 9. Extend()
# --------------------------------------------------
print("\n9. extend()")

numbers.extend([90,100,110])
print(numbers)

# --------------------------------------------------
# 10. Remove()
# --------------------------------------------------
print("\n10. remove()")

numbers.remove(25)
print(numbers)

# --------------------------------------------------
# 11. Pop()
# --------------------------------------------------
print("\n11. pop()")

removed = numbers.pop()

print("Removed :", removed)
print(numbers)

# --------------------------------------------------
# 12. Clear()
# --------------------------------------------------
print("\n12. clear()")

temp = [1,2,3]

temp.clear()

print(temp)

# --------------------------------------------------
# 13. Length
# --------------------------------------------------
print("\n13. len()")

print(len(numbers))

# --------------------------------------------------
# 14. Maximum & Minimum
# --------------------------------------------------
print("\n14. max() and min()")

print("Maximum :", max(numbers))
print("Minimum :", min(numbers))

# --------------------------------------------------
# 15. Sum
# --------------------------------------------------
print("\n15. sum()")

print(sum(numbers))

# --------------------------------------------------
# 16. Sort
# --------------------------------------------------
print("\n16. sort()")

marks = [90,65,78,99,45]

marks.sort()

print(marks)

# --------------------------------------------------
# 17. Reverse
# --------------------------------------------------
print("\n17. reverse()")

marks.reverse()

print(marks)

# --------------------------------------------------
# 18. Membership Operators
# --------------------------------------------------
print("\n18. Membership")

if 90 in marks:
    print("90 Found")

if 50 not in marks:
    print("50 Not Found")

# --------------------------------------------------
# 19. Loop Through List
# --------------------------------------------------
print("\n19. Loop Through List")

for item in fruits:
    print(item)

# --------------------------------------------------
# 20. Nested List
# --------------------------------------------------
print("\n20. Nested List")

students = [
    ["Guru",21],
    ["Rahul",22],
    ["Priya",20]
]

print(students)

print(students[0])

print(students[1][0])

# --------------------------------------------------
# 21. List Comprehension
# --------------------------------------------------
print("\n21. List Comprehension")

square = [x*x for x in range(1,6)]

print(square)

# --------------------------------------------------
# 22. Copy List
# --------------------------------------------------
print("\n22. Copy List")

copy_list = fruits.copy()

print(copy_list)

# --------------------------------------------------
# 23. Count
# --------------------------------------------------
print("\n23. count()")

values = [10,20,10,30,10]

print(values.count(10))

# --------------------------------------------------
# 24. Index
# --------------------------------------------------
print("\n24. index()")

print(values.index(30))

# --------------------------------------------------
# 25. Real World Example
# --------------------------------------------------
print("\n25. Student Marks")

marks = [85,90,78,88,95]

print("Marks :", marks)

print("Highest :", max(marks))
print("Lowest :", min(marks))
print("Average :", sum(marks)/len(marks))

print("\n========== END OF PROGRAM ==========")