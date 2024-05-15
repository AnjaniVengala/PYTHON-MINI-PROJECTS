weight = float(input("Enter your weight in Kg: "))
height = float(input("Enter your height in centimeters: "))
height = height / 100
BMI = weight /(height**2)
print("Your Body Mass Index is :", BMI)
if BMI <= 0:
    print("Please enter valid details")
else:
    if BMI < 15:
        print("Your are severely under weight")
    elif BMI >= 15 and BMI <= 18.5:
        print("You are under weight")
    elif BMI > 18.5 and BMI <= 25:
        print("You are healthy")
    elif BMI > 25:
        print("You are overweight")
