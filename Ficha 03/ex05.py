# adapt the last exercise so it asks if the player wants to try again (Y/N)

import random

random_number = random.randint(1,50)

awnser = "Y"
while awnser.upper() == "Y":
    print("\n\n\n\t\t\tWELCOME TO THE GAME-SHOW!!")
    print("\n\n\tTo play, please guess a number between 1 and 50. Good Luck!")

    attempt = 1
    guess = int(input("\n\tYour Guess: "))

    while random_number != guess and attempt <10:
        if random_number < guess:
            print("The random number is lower!")
        elif random_number > guess:
            print("The random number is higher!")
        guess = int(input("\n\tYour Guess: "))
        attempt += 1

    if random_number == guess:
        print("\n\n\n\n\n\n\t\tCongratulations! You found the number in {0} attempts!\n\n".format(attempt))
    else:
        print("\n\n\n\n\n\n\t\tI'm sorry you're out of attempts. Better Luck Next Time!\n\n")

    
awnser = input("Wanna play again? (Y/N): ")
print("\n\n\n\n\t\t\tThank you for playing!\n\n\n")

input()