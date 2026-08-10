# ==========================================
# PYTHON STRINGS - COMPLETE EXAMPLES
# ==========================================


# 1. Creating a string

name = "Guru"

print("Name:", name)


# 2. String length

print("\nLength:", len(name))


# 3. Accessing characters

print("First character:", name[0])
print("Last character:", name[-1])


# 4. String slicing

text = "Python Programming"

print("\nOriginal:", text)
print("First 6 characters:", text[:6])
print("Programming:", text[7:])
print("Reverse:", text[::-1])


# 5. Changing uppercase and lowercase

message = "Python is Powerful"

print("\nUppercase:", message.upper())
print("Lowercase:", message.lower())
print("Title:", message.title())
print("Capitalize:", message.capitalize())


# 6. Removing spaces

text = "   Python Programming   "

print("\nOriginal:", text)
print("After strip:", text.strip())
print("Left strip:", text.lstrip())
print("Right strip:", text.rstrip())


# 7. Finding text

sentence = "Python is easy to learn"

print("\nPosition of 'easy':",
      sentence.find("easy"))

print("Position of 'Python':",
      sentence.find("Python"))


# 8. Checking if text exists

if "Python" in sentence:
    print("Python is present")


# 9. Replacing text

sentence = "I love Java"

new_sentence = sentence.replace("Java", "Python")

print("\nOriginal:", sentence)
print("Updated:", new_sentence)


# 10. Splitting a string

data = "Python,Machine Learning,AI,Data Science"

items = data.split(",")

print("\nSplit data:")
print(items)


# 11. Joining strings

words = ["Python", "is", "easy"]

result = " ".join(words)

print("\nJoined string:")
print(result)


# 12. Checking string content

number = "12345"

print("\nIs digit:", number.isdigit())

word = "Python"

print("Is alphabet:", word.isalpha())

mixed = "Python123"

print("Is alphanumeric:", mixed.isalnum())


# 13. Counting characters

text = "programming"

print("\nNumber of 'm':",
      text.count("m"))


# 14. String formatting using f-string

name = "Guru"
age = 22
cgpa = 8.15

print("\nStudent Information:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {cgpa}")


# 15. Multiple string formatting

name = "Guru"
skill = "Machine Learning"

message = f"{name} is learning {skill}"

print("\n", message)


# 16. Escape characters

print("\nHello\nPython")
print("Python\tProgramming")


# 17. Comparing strings

language = "Python"

if language == "Python":
    print("\nThe language is Python")


# 18. Looping through a string

word = "AI"

print("\nCharacters:")

for character in word:
    print(character)


# 19. Practical example - cleaning text

user_input = "   GURU IS LEARNING PYTHON   "

cleaned_text = user_input.strip().lower()

print("\nOriginal text:")
print(user_input)

print("Cleaned text:")
print(cleaned_text)


# 20. Practical example - word count

sentence = "Python is very useful for Machine Learning"

words = sentence.split()

print("\nSentence:", sentence)
print("Number of words:", len(words))