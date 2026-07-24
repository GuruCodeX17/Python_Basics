# ==========================================
# Program 1: Print Numbers from 1 to 10
# ==========================================

print("Program 1")

for i in range(1, 11):
    print(i)


# ==========================================
# Program 2: Print Your Name 5 Times
# ==========================================

print("\nProgram 2")

name = input("Enter your name: ")

for i in range(5):
    print(name)


# ==========================================
# Program 3: Multiplication Table
# ==========================================

print("\nProgram 3")

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")


# ==========================================
# Program 4: Sum of Numbers from 1 to 100
# ==========================================

print("\nProgram 4")

sum = 0

for i in range(1, 101):
    sum += i

print("Sum =", sum)


# ==========================================
# Program 5: Even Numbers
# ==========================================

print("\nProgram 5")

for i in range(2, 21, 2):
    print(i)


# ==========================================
# Program 6: Odd Numbers
# ==========================================

print("\nProgram 6")

for i in range(1, 21, 2):
    print(i)