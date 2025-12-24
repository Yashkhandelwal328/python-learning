# Membership operators = used to test wether a value or variable is found in a sequence
#                        (string, list, set, or dictionary)
#                        1. in
#                        2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"there is a '{letter}'")
else:
    print(f"{letter} not found")

students = {"Spongebob","Patrick","Sandy"}

student = input("Enter the name of student")

if student in students:
    print("yes")
else :
    print("no")

grades={"Sandy":"A",
        "Squidward":"B",
        "Spongebob":"C"
         }

student = input("Enter the name of a Student")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found") 