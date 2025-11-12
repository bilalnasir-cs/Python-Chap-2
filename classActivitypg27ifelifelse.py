'''
Write an if-elif-else statement to check whether a number is positive , negative or zero.
'''
print("+ve/-ve/Zero Checker")
print("****************")

number = int(input("Enter an integer:"))

if number > 0:
    print(number,"is +ve")
elif number < 0:
    print(number,"is -ve")
else:
    print(number,"is zero")