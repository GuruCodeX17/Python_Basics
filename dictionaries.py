# ==========================================
# PYTHON DICTIONARIES - COMPLETE EXAMPLES
# ==========================================

# 1. Creating a dictionary

student = {
    "name": "Guru",
    "age": 22,
    "department": "CSE",
    "cgpa": 8.15
}

print("Student:", student)


# 2. Accessing values

print("\nName:", student["name"])
print("Department:", student["department"])


# 3. Using get()

print("CGPA:", student.get("cgpa"))
print("College:", student.get("college", "Not Available"))


# 4. Adding a new key-value pair

student["college"] = "Adhiparasakthi College of Engineering"

print("\nAfter adding college:")
print(student)


# 5. Updating a value

student["cgpa"] = 8.25

print("\nUpdated CGPA:", student["cgpa"])


# 6. Updating multiple values

student.update({
    "age": 23,
    "city": "Ranipet"
})

print("\nAfter updating:")
print(student)


# 7. Removing an item using pop()

student.pop("city")

print("\nAfter removing city:")
print(student)


# 8. Removing the last item using popitem()

student.popitem()

print("\nAfter popitem:")
print(student)


# 9. Checking if a key exists

if "name" in student:
    print("\nName key exists")


# 10. Getting all keys

print("\nKeys:")
print(student.keys())


# 11. Getting all values

print("\nValues:")
print(student.values())


# 12. Getting key-value pairs

print("\nItems:")
print(student.items())


# 13. Loop through keys

print("\nDictionary Keys:")

for key in student:
    print(key)


# 14. Loop through values

print("\nDictionary Values:")

for value in student.values():
    print(value)


# 15. Loop through key-value pairs

print("\nKey-Value Pairs:")

for key, value in student.items():
    print(key, ":", value)


# 16. Dictionary length

print("\nNumber of items:", len(student))


# 17. Nested dictionary

students = {
    "student1": {
        "name": "Guru",
        "cgpa": 8.15
    },

    "student2": {
        "name": "Arun",
        "cgpa": 8.50
    },

    "student3": {
        "name": "Kumar",
        "cgpa": 7.90
    }
}

print("\nNested Dictionary:")
print(students)


# 18. Accessing nested dictionary

print("\nStudent 1 Name:",
      students["student1"]["name"])

print("Student 2 CGPA:",
      students["student2"]["cgpa"])


# 19. Dictionary from two lists

names = ["Guru", "Arun", "Kumar"]
marks = [85, 90, 78]

student_marks = dict(zip(names, marks))

print("\nStudent Marks:")
print(student_marks)


# 20. Practical example

employee = {
    "name": "Guru",
    "role": "AI Engineer",
    "skills": ["Python", "Machine Learning", "SQL"],
    "experience": 0
}

print("\nEmployee Information:")
print("Name:", employee["name"])
print("Role:", employee["role"])
print("Skills:", employee["skills"])
print("Experience:", employee["experience"])