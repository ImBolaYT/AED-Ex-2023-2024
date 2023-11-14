# program that simulates factorial functions
# Example: Factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120
# Note that 0! = 1

num = int(input("Insert a number: "))

while num < 0:
    print("\nPlease only insert integer numbers bigger than 0!")
    num = int(input("\nInsert a number: "))

factorial = 1
for i in range(1, num+1):
    factorial*=i

print("\n\tThe factorial of {0} is {1} .\n".format(num, factorial))