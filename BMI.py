'''
Write a program to calculate the Body Mass Index (BMI).
The formula is: BMI=weight(kg)/
height(m)^2
Steps:
1. Ask the user for their weight (in kilograms).
2. Ask the user for their height (in meters).
3. Compute their BMI.
4. Print the BMI and its classification.
'''
print("BMI Calculator")
print("**************")

#input weight(kg) and height(meters)
#Weight and height can be floating point values

#Step 1.
weight=float(input("Enter your weight(kg):"))

#Step 2.
height=float(input("Enter your height(meters):"))

#Step 3.
BMI = weight / (height * height)

#Step 4.
print("Your BMI is",BMI,"kg/m^2");
print("Classification:")
print("BMI Category \t BMI Range")
print("UnderWeight \t Less than 18.5")
print("Healthy Weight \t 18.5 to less than 25")
print("Overweight \t 25 to less than 30")
print("Obesity \t 30 or greater")

