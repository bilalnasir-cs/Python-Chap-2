#Write an if else and short hand if else statement to check 
#if a number is even or odd and print the appropriate message.

number = int(input("Enter an integer:"))

if number % 2 == 0:
    print("Number is Even.")
else:
    print("Number is Odd.")

print("Number is Even") if number % 2 == 0 else print("Number is Odd.")

checkOddEven = "Number is Even" if number % 2 == 0 else "Number is Odd."
print(checkOddEven)