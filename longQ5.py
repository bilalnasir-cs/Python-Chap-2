'''
Write a python program that takes a number as input
and checks whether it is positive, negative, or zero
using an if-elif-else statement.
'''

number = int(input("Enter an integer:"))

if number > 0 :
    print("Number is positive")
elif number < 0 :
    print("Number is negative")
else:
    print("Number is zero")