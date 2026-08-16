# Object-Oriented Programming (OOP) in Python

class Student:

    # Constructor
    def __init__(self, name, age, department, marks):
        self.name = name
        self.age = age
        self.department = department
        self.marks = marks

    # Method to display student details
    def display_details(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Marks:", self.marks)

    # Method to check result
    def check_result(self):
        if self.marks >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")

    # Method to calculate grade
    def calculate_grade(self):
        if self.marks >= 90:
            grade = "A+"
        elif self.marks >= 80:
            grade = "A"
        elif self.marks >= 70:
            grade = "B"
        elif self.marks >= 60:
            grade = "C"
        elif self.marks >= 50:
            grade = "D"
        else:
            grade = "F"

        print("Grade:", grade)


# Creating objects
student1 = Student("Guru", 21, "Computer Science", 85)
student2 = Student("Arun", 22, "Information Technology", 72)

# Student 1
print("----- Student 1 -----")
student1.display_details()
student1.check_result()
student1.calculate_grade()

print()

# Student 2
print("----- Student 2 -----")
student2.display_details()
student2.check_result()
student2.calculate_grade()