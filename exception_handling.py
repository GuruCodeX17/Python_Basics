# ==========================================
# PYTHON EXCEPTION HANDLING - EXAMPLES
# ==========================================


# 1. Basic try-except

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Please enter a valid number.")


# 2. Handling division by zero

try:
    a = 10
    b = 0

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")


# 3. Multiple exceptions

try:
    number = int(input("\nEnter another number: "))
    result = 100 / number

    print("Result:", result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Number cannot be zero.")


# 4. try-except-else

try:
    number = int(input("\nEnter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("Successfully converted:", number)


# 5. try-except-finally

try:
    number = int(input("\nEnter a number: "))

except ValueError:
    print("Invalid input.")

finally:
    print("This block always executes.")


# 6. Handling list index error

numbers = [10, 20, 30]

try:
    print("\nNumber:", numbers[5])

except IndexError:
    print("Index does not exist.")


# 7. Handling dictionary key error

student = {
    "name": "Guru",
    "age": 22
}

try:
    print("\nCollege:", student["college"])

except KeyError:
    print("College key does not exist.")


# 8. Catching a general exception

try:
    result = 10 / 0

except Exception as error:
    print("\nAn error occurred:", error)


# 9. Using raise

age = 15

try:
    if age < 18:
        raise ValueError("Age must be 18 or above.")

except ValueError as error:
    print("\nError:", error)


# 10. Practical example - user input

try:
    mark = int(input("\nEnter your mark: "))

    if mark < 0 or mark > 100:
        raise ValueError("Mark must be between 0 and 100.")

    print("Your mark:", mark)

except ValueError as error:
    print("Invalid input:", error)


print("\nProgram completed successfully!")