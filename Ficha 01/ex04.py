# Calculate the IBC from Weight and Height
# IBC = Weight/Height^2

weight = float(input("Weight (kg):"))
height =float(input("Height(m):"))

ibc = weight / (height**2)

print("IBC = {:.2f}" .format(ibc))

input()