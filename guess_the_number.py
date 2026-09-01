import random

number = random.randint(1, 100)
guesses = 0

print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    guesses = guesses + 1

    if guess > number:
        print("Lower number please")

    elif guess < number:
        print("Higher number please")

    else:
        print("Congratulations! You guessed the correct number.")
        print("You guessed the number in", guesses, "guesses.")
        break
    