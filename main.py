import random
from number_guess_art import logo
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")

number = random.randint(1,101)
# print(f"Psssst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    tries = 10
elif difficulty == "hard":
    tries = 5
else:
    print("Enter a valid difficulty level.")

attempt = 0
continue_game = True
while attempt < tries and continue_game:
    print(f"You have {tries-attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    elif guess == number:
        print(f"You got it. The answer was {guess}.")
        continue_game = False
    attempt += 1
    if attempt != 5 and continue_game:
        print("Guess_again")
    elif attempt == 5  and guess != number:
        print("Game Over.")