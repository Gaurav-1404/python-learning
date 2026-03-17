# Water, snake, gun game
import random

def game():
    print("Snake Water Gun Game")
    print("s = Snake, w = Water, g = Gun")

    choices = ["s", "w", "g"]
    computer = random.choice(choices)
    user = input("Enter your choice: ")

    if user not in choices:
        print("Invalid input!")
        return

    print("Computer chose:", computer)

    if user == computer:
        print("It's a draw!")
    elif (user == "s" and computer == "w") or \
         (user == "w" and computer == "g") or \
         (user == "g" and computer == "s"):
        print("You win!")
    else:
        print("You lose!")

game()