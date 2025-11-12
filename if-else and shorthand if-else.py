'''
Write an if else statement and short-hand if else statement to check if the number
is even or odd and print the appropriate message.
'''

print("Odd/Even Checker")
print("****************")

number = int(input("Enter an integer:"))

if number % 2 == 0:
    print(number," is even")
else:
    print(number,"is odd")
    
print(number,"is even") if number % 2 == 0 else print(number,"is odd")