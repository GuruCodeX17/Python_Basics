# ==========================================
# WHILE LOOP PROGRAMS
# ==========================================

# ==========================================
# Program 1: Print Numbers from 1 to 10
# ==========================================

print("========== Program 1 ==========")
print("Numbers from 1 to 10")

i = 1
while i <= 10:
    print(i)
    i += 1


# ==========================================
# Program 2: Print Your Name 5 Times
# ==========================================

print("\n========== Program 2 ==========")

name = input("Enter your name: ")

count = 1
while count <= 5:
    print(name)
    count += 1


# ==========================================
# Program 3: Multiplication Table
# ==========================================

print("\n========== Program 3 ==========")

num = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1


# ==========================================
# Program 4: Sum of Numbers from 1 to 100
# ==========================================

print("\n========== Program 4 ==========")

total = 0
i = 1

while i <= 100:
    total += i
    i += 1

print("Sum of numbers from 1 to 100 =", total)


# ==========================================
# Program 5: Even Numbers from 1 to 20
# ==========================================

print("\n========== Program 5 ==========")

i = 2

while i <= 20:
    print(i)
    i += 2


# ==========================================
# Program 6: Odd Numbers from 1 to 20
# ==========================================

print("\n========== Program 6 ==========")

i = 1

while i <= 20:
    print(i)
    i += 2

print("\nAll while loop programs completed successfully!")