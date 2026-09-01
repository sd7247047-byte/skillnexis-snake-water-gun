import random

print("Snake Water Gun Game")
print("Let's play!")

choices = ["snake", "water", "gun"]

while True:
    user = input("\nEnter your choice (snake/water/gun): ").lower()

    if user not in choices:
        print("Invalid choice! Please enter snake, water, or gun.")
        continue

    computer = random.choice(choices)

    print("you chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "snake" and computer == "water") or \
            (user == "water" and computer == "gun") or \
            (user == "gun" and computer == "snake"):
        print("You win!")

    else:
        print("Computer wins!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
    