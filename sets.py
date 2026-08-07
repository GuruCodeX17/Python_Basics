# ==========================================
# PYTHON SETS - COMPLETE EXAMPLES
# ==========================================

# 1. Creating a set
fruits = {"apple", "banana", "orange", "mango"}
print("Set:", fruits)


# 2. Duplicate values are automatically removed
numbers = {10, 20, 20, 30, 30, 40}
print("\nSet with duplicates removed:", numbers)


# 3. Adding an element
fruits.add("grape")
print("After adding grape:", fruits)


# 4. Adding multiple elements
fruits.update(["watermelon", "papaya"])
print("After adding multiple fruits:", fruits)


# 5. Removing an element
fruits.remove("banana")
print("After removing banana:", fruits)


# 6. Discarding an element
fruits.discard("kiwi")
print("After discard:", fruits)


# 7. Checking if an element exists
if "apple" in fruits:
    print("\nApple is available")


# 8. Looping through a set
print("\nFruits:")
for fruit in fruits:
    print(fruit)


# 9. Union
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("\nSet A:", set_a)
print("Set B:", set_b)
print("Union:", set_a.union(set_b))


# 10. Intersection
print("Intersection:", set_a.intersection(set_b))


# 11. Difference
print("A - B:", set_a.difference(set_b))
print("B - A:", set_b.difference(set_a))


# 12. Symmetric difference
print("Symmetric Difference:",
      set_a.symmetric_difference(set_b))


# 13. Set length
print("Number of elements in A:", len(set_a))


# 14. Converting list to set
my_list = [1, 2, 2, 3, 3, 4, 5]

unique_values = set(my_list)

print("\nOriginal list:", my_list)
print("Unique values:", unique_values)


# 15. Practical example
students_python = {"Guru", "Arun", "Kumar", "Priya"}
students_java = {"Kumar", "Priya", "Rahul"}

print("\nStudents learning Python:", students_python)
print("Students learning Java:", students_java)

print("Students learning both:",
      students_python.intersection(students_java))

print("Students learning either Python or Java:",
      students_python.union(students_java))