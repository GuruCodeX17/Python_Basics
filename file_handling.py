# ==========================================
# PYTHON FILE HANDLING - COMPLETE EXAMPLES
# ==========================================


# 1. Create and write to a file
with open("student.txt", "w") as file:
    file.write("Name: Guru\n")
    file.write("Department: CSE\n")
    file.write("CGPA: 8.15\n")

print("File created and data written successfully.")


# 2. Read the complete file
with open("student.txt", "r") as file:
    content = file.read()

print("\n--- File Content ---")
print(content)


# 3. Read the file line by line
print("--- Reading Line by Line ---")

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())


# 4. Read all lines into a list
with open("student.txt", "r") as file:
    lines = file.readlines()

print("\n--- Lines as List ---")
print(lines)


# 5. Append new data
with open("student.txt", "a") as file:
    file.write("Skill: Python\n")

print("New data appended successfully.")


# 6. Read the updated file
with open("student.txt", "r") as file:
    updated_content = file.read()

print("\n--- Updated File ---")
print(updated_content)


# 7. Write multiple lines using writelines()
additional_data = [
    "Skill: Machine Learning\n",
    "Skill: Data Science\n"
]

with open("student.txt", "a") as file:
    file.writelines(additional_data)

print("Multiple lines added successfully.")


# 8. Check whether a file exists
import os

if os.path.exists("student.txt"):
    print("\nstudent.txt exists.")
else:
    print("\nstudent.txt does not exist.")


# 9. Get file size
if os.path.exists("student.txt"):
    size = os.path.getsize("student.txt")
    print("File size:", size, "bytes")


# 10. Create another file
with open("skills.txt", "w") as file:
    file.write("Python\n")
    file.write("Machine Learning\n")
    file.write("GitHub\n")

print("\nskills.txt created successfully.")


# 11. Read another file
with open("skills.txt", "r") as file:
    skills = file.read()

print("\n--- Skills ---")
print(skills)


# 12. Practical example - storing student information

students = [
    "Guru - CSE - 8.15\n",
    "Arun - CSE - 8.50\n",
    "Kumar - CSE - 7.90\n"
]

with open("students.txt", "w") as file:
    file.writelines(students)

print("Student data saved successfully.")


# 13. Read student data

print("\n--- Student Data ---")

with open("students.txt", "r") as file:
    for student in file:
        print(student.strip())


# 14. Exception handling with file handling

try:
    with open("unknown.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("\nError: The requested file was not found.")


print("\nFile handling program completed successfully!")