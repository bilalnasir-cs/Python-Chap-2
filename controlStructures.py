#if statement
temperature = 35
if temperature > 30:
    print("It's a hot day.")

#if else statement
temperature = 15
if temperature > 30:
    print("It's a hot day.")
else:
    print("It's not a hot day.")

#Short hand if else

temperature = 15
m = "It's a hot day." if temperature > 30 else "It's not a hot day."
print(m)