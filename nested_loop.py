# ==========================================
# NESTED LOOP PROGRAMS
# ==========================================

# ==========================================
# Program 1: Multiplication Tables (1 to 10)
# ==========================================

print("========== Program 1 ==========")

for i in range(1, 11):
    print(f"\nTable of {i}")

    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")


# ==========================================
# Program 2: Student Marks
# ==========================================

print("\n========== Program 2 ==========")

students = ["Guru", "Rahul", "Arun"]
subjects = ["Math", "Science", "English"]

for student in students:
    print(f"\nMarks for {student}")

    for subject in subjects:
        mark = int(input(f"Enter {subject} mark: "))
        print(subject, ":", mark)


# ==========================================
# Program 3: Seating Arrangement
# ==========================================

print("\n========== Program 3 ==========")

for row in range(1, 6):
    for seat in range(1, 5):
        print(f"R{row}S{seat}", end=" ")
    print()


# ==========================================
# Program 4: Mini Calendar
# ==========================================

print("\n========== Program 4 ==========")

for week in range(1, 5):
    print(f"Week {week}")

    for day in range(1, 8):
        print(f"Day {day}")

    print()


# ==========================================
# Program 5: Matrix
# ==========================================

print("\n========== Program 5 ==========")

matrix = [
    [1, 2],
    [3, 4]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()


# ==========================================
# Program 6: Star Pattern
# ==========================================

print("\n========== Program 6 ==========")

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nNested loop programs completed successfully!")