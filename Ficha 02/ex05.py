# Program that read 3 numbers and prints them in ascending order

num1 = int(input("Insert 1st number: "))
num2 = int(input("Insert 2nd number: "))
num3 = int(input("Insert 3rd number: "))

if num1 < num2:
    if num2 < num3:
        print(num1, num2, num3)
    elif num1 < num3:
        print(num1, num3, num2)
    else:
        print(num3, num1, num2)
elif num2 < num3:
    if num1 < num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    print(num3, num2, num1)

input()