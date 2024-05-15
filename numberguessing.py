import random
import math

# Welcome message
print("Welcome to the Number Guessing Game!")

# Input validation for lower bound
while True:
    try:
        lower = int(input("Enter Lower bound: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Input validation for upper bound
while True:
    try:
        upper = int(input("Enter Upper bound: "))
        if upper <= lower:
            print("Please enter a number greater than the lower bound.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Generating a random number between the lower and upper bounds
x = random.randint(lower, upper)
max_attempts = round(math.log(upper - lower + 1, 2))
print(f"\n\tYou have {max_attempts} chances to guess the integer!\n")

count = 0

while count < max_attempts:
    count += 1
    
    # Input validation for guessing
    while True:
        try:
            guess = int(input(f"Guess a number between {lower} and {upper}: "))
            if guess < lower or guess > upper:
                print(f"Please enter a number between {lower} and {upper}.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Checking the guessed number
    if x == guess:
        print(f"Congratulations! You guessed the number in {count} tries.")
        break
    elif x > guess:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")

if count >= max_attempts:
    print(f"\nYou've used all your attempts. The number was {x}.")
    print("Better luck next time!")
