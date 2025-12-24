# while loop = execute some code WHILE some condition remains true 
name = input("Enter your name: ")

while name == "":
    print("you did not enter your name ")
    name = input("Enter your name")

print(f"Hello {name}")

# Another Example
age = int(input("Enter your age: "))

while age<0:
    print("Age can't be negetive")
    age = int(input("Enter your age"))

print(f"You are {age} years old")
 
#  Another Example
food = input("Enter a food you like (q to quit)")

while food != "q":
    print(f"you like {food}")
    food = input("Enter a another food you like ")

# Another example

num = int(input("Enter a number from 1 - 10"))

while num < 1 or num > 10 :
    print("You entered a invalid number")
    num = int(input("Enter a number from 1 - 10"))

print(f"Your number is {num}")

print('bye')