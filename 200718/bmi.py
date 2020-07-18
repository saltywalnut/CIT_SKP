def bmi_calculator(weight , height):
    return weight / (height ** 2)

mode = "active"

while mode != "close" :
    userWeight = int ( input ("type your weight in kilograms: ") )
    userHeight = float (input ("type your height in metres: ") )
    print ( bmi_calculator(userWeight, userHeight))
    mode = input ("Type something to continue")

print("program shutdown successful")
