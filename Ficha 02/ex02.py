# Program that allows to classify a triangle by reading the 3 sides
# equilateral: all sides are equal.
# isosceles: two sides equal.
# scalene: all sides are different

side1 = int(input("Introduce the 1st side: "))
side2 = int(input("Introduce the 2nd side: "))
side3 = int(input("Introduce the 3rd side: "))

if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

input()