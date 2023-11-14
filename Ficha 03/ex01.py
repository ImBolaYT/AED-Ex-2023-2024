# program that reads 10 numbers and indicates the largest and the average

import math

biggest = -math.inf

add = 0
for i in range(10):
    number = int(input("Insert the number: "))
    add+=number
    if number > biggest:
        biggest = number

print("The media is {:.2f} !".format(add/10))
print("The biggest number is {:.2f} !".format(biggest))