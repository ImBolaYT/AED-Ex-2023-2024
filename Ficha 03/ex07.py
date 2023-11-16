# Program that reads a number (integer and positive) and indicates if it's a prime number or not
# Prime numbers can only be divided by itself and 1

num = int(input("Insert a number: "))

prime = True
for i in range(2, num):
    left = num % i
    if left == 0:
        prime = False
        break

if prime == True:
    print("The number {0} is a prime number." .format(num))
else:
    print("The number {0} is NOT a prime number." .format(num))

input()