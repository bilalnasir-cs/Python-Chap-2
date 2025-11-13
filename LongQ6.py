'''
Write a Python program using a while loop that prints
all the odd numbers between 1 and 100.
Also, count and print the total number of odd numbers.
'''

i = 1
count = 0
while i <= 100:
    print(i)
    i += 2
    count += 1

print("Total odd numbers between 1 and 100 are",count)
