import random
#Generate a random number between 1 and 19
number = random.randint(1,10)
print("The random number is : ",number)

import datetime
#Get the current date and time
current_time= datetime.datetime.now()
print("Current date and time:",current_time)

import statistics
#Calculate the mean of a list of numbers
data = [23,45,67,89,12,44,56]
mean_value = statistics.mean(data)
print("The mean value is : ", mean_value)