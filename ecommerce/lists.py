#Creating a list of items
fruits = ["Mango","Apple","Banana"]
print(fruits)

#Accessing a list item by index
print(fruits[1])

#modifying a List
fruits[0] = "Orange"
fruits.append("Pineapple")
print(fruits)

#Methods and Operations on Lists

students = ["Ahmed","Sara","Ali"]
print(students)
students.append("Hina")
print(students)
students.sort()
print(students)

#Slice a portion of the list and concatenate with another list
number = [1,2,3,4,5]
number_slice = numbers[1:4]
print(number_slice)

extra_numbers = [6,7]
combined = number_slice + extra_numbers
print(combined)

#Sort a list of student names and remove a specific name

student_name = ["Ahmed","Sara","Ali","Hina"]
print(student_name)
student_name.sort()
print(student_name)
student_name.remove("Sara")
print(student_name)