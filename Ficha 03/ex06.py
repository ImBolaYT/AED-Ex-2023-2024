# A Program that allows me to generate a random number between 1900 and 2020 and tell the user if it's a leap year or not
# Leap Years are divided by 4 but can't be divided by 100 unless it's divided by 400
# In the end it asks the user if he wants to generate a new random number

import random

awnser = "Y"
while awnser.upper() == "Y":
    random_year = random.randint(1900,2020)
    print("\n\t\t", random_year,)
    if (random_year % 400 == 0) or (random_year % 4 == 0 and random_year % 100 != 0):
        print("\n\t{0} is a leap year".format(random_year))
    else:
        print("\n\t{0} is not a leap year".format(random_year))

    awnser = input("\n\tGenerate a new number?(Y/N):") 