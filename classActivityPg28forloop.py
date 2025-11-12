#Write a for loop using range() to print even numbers from 2 to 10
for i in range(2,11,2):
    print(i)

for i in range(2,11):
    if i % 2 == 0:
        print(i)

# First 10 multiples of 3 using for loop and range() function

for i in range(1,11):
    print(3,"*",i,"=",3*i)