def greet(name):
    print("Hello,",name)

#Function Parameters and Return Values

def add(a,b):
    return a+b

#Default Paramters

def greeting(name="Student"):
    return "Hello " + name + "!"

#Function call
greet("Ali")
greet("Bilal")


sum = add(2,3)
print(sum)
sum = add(5,7)
print(sum)

print(greeting())
print(greeting("Umer"))