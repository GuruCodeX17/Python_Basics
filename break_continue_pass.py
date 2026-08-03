# ==========================================
# BREAK, CONTINUE, PASS - PYTHON PROGRAMS
# ==========================================

# ==========================================
# Program 1 : break
# ==========================================

print("========== Program 1 : break ==========")

for i in range(1, 11):
    if i == 6:
        break
    print(i)

print()


# ==========================================
# Program 2 : continue
# ==========================================

print("========== Program 2 : continue ==========")

for i in range(1, 11):
    if i == 6:
        continue
    print(i)

print()


# ==========================================
# Program 3 : pass
# ==========================================

print("========== Program 3 : pass ==========")

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

print()


# ==========================================
# Program 4 : Password Checking (break)
# ==========================================

print("========== Program 4 : Password Checking ==========")

password = "python123"

while True:
    user = input("Enter Password: ")

    if user == password:
        print("Access Granted")
        break

    print("Wrong Password. Try Again.")

print()


# ==========================================
# Program 5 : Print Only Odd Numbers (continue)
# ==========================================

print("========== Program 5 : Print Only Odd Numbers ==========")

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)

print()


# ==========================================
# Program 6 : Search a Number (break)
# ==========================================

print("========== Program 6 : Search Number ==========")

numbers = [12, 25, 30, 45, 60]

search = int(input("Enter number to search: "))

found = False

for num in numbers:
    if num == search:
        print("Number Found")
        found = True
        break

if not found:
    print("Number Not Found")

print("\nAll Break, Continue and Pass programs completed successfully!")1707