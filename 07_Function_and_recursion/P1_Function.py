# defination of function
def avg():
    b = int(input("Enter any number: "))
    a = int(input("Enter any number: "))
    c = int(input("Enter any number: "))
    avg = (a+b+c)/3
    return avg

# function Calling
a = avg()
print(a)


def greet(name, ending = "Thankyou!"):
    print("Hello",name)
    print(ending)

# program to greet a user by name
name = input("Enter your name: ")
greet(name , "Thanks!")
greet("Rahul")

# Two types of function in python
# 1. Built in function   2. User define function
