# ==============================
# PYTHON DICTIONARY
# ==============================

print("========== PYTHON DICTIONARY ==========\n")

# 1. Create Dictionary
student = {
    "Name": "Guru",
    "Age": 20,
    "Department": "CSE",
    "CGPA": 8.15
}

print("1. Original Dictionary")
print(student)

# 2. Access Values
print("\n2. Access Values")
print("Name:", student["Name"])
print("Department:", student["Department"])

# 3. Using get()
print("\n3. Using get()")
print(student.get("Age"))

# 4. Add New Item
print("\n4. Add New Item")
student["College"] = "Adhiparasakthi College of Engineering"
print(student)

# 5. Update Value
print("\n5. Update Value")
student["CGPA"] = 8.50
print(student)

# 6. Remove Item
print("\n6. Remove Item")
student.pop("Age")
print(student)

# 7. Dictionary Keys
print("\n7. Keys")
print(student.keys())

# 8. Dictionary Values
print("\n8. Values")
print(student.values())

# 9. Dictionary Items
print("\n9. Items")
print(student.items())

# 10. Loop Through Dictionary
print("\n10. Loop Through Dictionary")

for key, value in student.items():
    print(key, ":", value)

# 11. Check Key Exists
print("\n11. Check Key")

if "Name" in student:
    print("Name exists")

# 12. Dictionary Length
print("\n12. Length")
print(len(student))

# 13. Copy Dictionary
print("\n13. Copy")
student_copy = student.copy()
print(student_copy)

# 14. Nested Dictionary
print("\n14. Nested Dictionary")

students = {
    "Student1": {
        "Name": "Guru",
        "CGPA": 8.5
    },
    "Student2": {
        "Name": "Rahul",
        "CGPA": 8.8
    }
}

print(students)

print("\n=========== END OF PROGRAM ===========")