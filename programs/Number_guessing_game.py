import random

lower_count = 1
upper_count = 100
answer = random.randint(lower_count,upper_count)

print("Welcome to Number Guessing Game")
print(f"You will have to picko a number between {lower_count} to {upper_count}")
is_running = True
guess = 0
difference = abs(answer - guess)



while is_running:
    guess = int(input("Enter your guess: "))
    if guess == answer:
        print("Congratulations you won ")
    elif lower_count > guess > upper_count:
        print(f"Invalid guess range is {lower_count} to {upper_count}")
    else:
        if guess > answer:
            print("Too high, keep guessing.")
        else:
                print("Too low, keep guessing.")

        