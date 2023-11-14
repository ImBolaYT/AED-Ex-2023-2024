# adapt the last exercise so the user asks how many numbers he wants to read

import math

biggest = -math.inf
add = 0
read = int(input("How many numbers do you want to read? "))
for i in range(read):
    number = int(input("Insert the number: "))
    add+=number
    if number > biggest:
        biggest = number

print("The media is {:.2f} !".format(add/read))
print("The biggest number is {:.2f} !".format(biggest))