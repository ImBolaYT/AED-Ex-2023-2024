# Program that receives Gender(M/F) and Height(cm) and gives back the Ideal weight
# Ideal weight = (h-100) - (h-150)/k 
# k = 2 female | k = 4 male | h = height

gender = input("Gender(M/F): ")
if gender.lower() != "m" and gender.lower() != "f":
    print("Invalid Gender")
    exit()
height = int(input("Altura(cm): "))

if gender.lower() == "m":
    k = 4
else:
    k = 2

ideal_weight = (height-100) - (height-150)/k

print("The ideal weight is {:.2f}Kg".format(ideal_weight))

input()