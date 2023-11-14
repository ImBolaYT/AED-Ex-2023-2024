# Guessing Game, generate a random number from 1 to 50, each attempt it should say if the number is higher/lower and if he wins he gets a "You got it" and "Congratulations" message
# After 10 attempts the game end saying "You have run out of attempts" and showing the correct number
# When it finds the correct number it shows the number of attempts

import random

random_number = random.randint(1,50)

print("\n\n\t\t\tWELCOME TO THE GAME-SHOW!!")
print("\n\n\tTo play, please guess a number between 1 and 50. Good Luck!")

attempt = 1
guess = int(input("\n\tYour Guess:"))

while random_number != guess and attempt <10:
    if random_number < guess:
        print("The random number is lower!")
    elif random_number > guess:
        print("The random number is higher!")
    guess = int(input("\n\tYour Guess:"))
    attempt += 1

if random_number == guess:
    print("\n\n\n\n\n\n\t\tCongratulations! You found the number in {0} attempts!\n\n\n".format(attempt))
else:
    print("\n\n\n\n\n\n\t\tI'm sorry you're out of attempts. Better Luck Next Time!\n\n\n")

input()