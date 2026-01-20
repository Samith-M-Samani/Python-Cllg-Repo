weight = int(input("Enter weight in kg: "))
height = int(input("Enter height in cm: "))

bmi = (weight * 10000) // (height * height)

print("Your BMI is:", bmi)

if bmi < 18:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
