# Project 2 : Guess the number guessing game!
import random

def guess_the_number():
    """Guess the number game by computer!"""
    number = random.randint(1, 100)
    guesses_left = 10
    
    # Welcome message
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    
    # Loop generated for guessing
    while guesses_left > 0:
        print(f"\nYou have only {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        # Check the guessed number
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You got the correct number in {10 - guesses_left + 1} tries.")
            break  # End the game when the correct number is guessed
        
        guesses_left -= 1  # Reduce guesses left
        
        # If no guesses are left, the game is over
        if guesses_left == 0:
            print(f"\nYou ran out of guesses. The number was {number}.")
            break  # End the game when no guesses are left

# Call the function to start the game
guess_the_number()
