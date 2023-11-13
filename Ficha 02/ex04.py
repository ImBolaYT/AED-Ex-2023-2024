# Individual Body Mass Index / asks for Weight(Kg) and Height(m)
# IMC = weight/height^2
#   < 18.5 Under weight
#   [18.5 – 25[ Healthy
#   [25 – 30[ Overweight
#   [30 – 35[ Obesity Grade I
#   [35 – 40[ Obesity Grade II (severe)
#   ≥ 40.0 Obesity Grade III (morbid)

weight = float(input("Insert your weight(Kg): "))
height = float(input("Insert your height(m): "))

ibm = weight / height**2
print("Your IBM is: {:.2f}".format(ibm))

if ibm < 18.5:
    print("Under weight.")
elif ibm <= 24.9:
    print("Healthy")
elif ibm <= 29.9:
    print("Overweight")
elif ibm <= 34.9:
    print("Obesity Grade I")
elif ibm <= 39.9:
    print("Obesity Grade II (severe)")
else:
    print("Obesity Grade III (morbid)")

input()