# implement a simulator of weight on another planet
#    Planet Code | Planet Relative | Gravity
#          1           Mercury         0.37
#          2           Venus           0.88
#          3           Mars            0.38
#          4           Jupiter         2.64
#          5           Saturn          1.15
#          6           Uranus          1.17

# ask for weight(kg) and the planet code

print("\t\t\t\tPlanets")
print("\t\t\t1 - Mercury")
print("\t\t\t2 - Venus")
print("\t\t\t3 - Mars")
print("\t\t\t4 - Jupiter")
print("\t\t\t5 - Saturn")
print("\t\t\t6 - Uranus")

weight = float(input("\n\tYour weight (kg): "))
code = int(input("\n\tPlanet code: "))

if code == 1:
    gravity = 0.37
elif code == 2:
    gravity = 0.88
elif code == 3:
    gravity = 0.38
elif code == 4:
    gravity = 2.64
elif code == 5:
    gravity = 1.15
elif code == 6:
    gravity = 1.17
else:
    print("invalid planet code!:( ")

weight_planet = weight*gravity
print("\n\tYour weight {:.2f} kg, on the planet {:.0f} would be {:.2f}" .format(weight, code, weight_planet))