# Program that works like a small cardiac effort simulator´
# MHR = 226 - age (female)
# MHR = 220 - age (men)

gender = input("\n\n\t\tGender(M/F): ")
if gender.lower() != "m" and gender.lower() != "f":
    print("Invalid Gender")
    exit()

age = int(input("\n\n\t\tAge: "))

if gender.lower() == "m":
    mhr = 220 - age
else:
    mhr = 226 - age

print("\n\n\t\tMHR= ",mhr," bpm\n\n\t\t")