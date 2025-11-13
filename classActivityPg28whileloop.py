'''
Write a python program that prints the even numbers
and count the odd numbers
from 1 to 20 
using a while loop.
'''
oddCount = 0
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    else:
        oddCount +=2
    
    i += 1

print("Total odd numbers between 1 and 20 = ",oddCount)
    