'''
1. Create a class “Programmer” for storing information of few programmers 
    working at Microsoft. 
2. Write a class “Calculator” capable of finding square, cube and square root of a 
    number. 
3. Create a class with a class attribute a; create an object from it and set ‘a’ 
    directly using ‘object.a = 0’. Does this change the class attribute? 
4. Add a static method in problem 2, to greet the user with hello. 
5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
    and get fare information of train running under Indian Railways. 
6. Can you change the self-parameter inside a class to something else (say 
    “harry”). Try changing self to “slf” or “harry” and see the effects. 
'''
# 1..
class Programmer:
    company = "Microsoft"
    def __init__(self, name, age, salary ):
        print("Programmer added successfully")
        self.name = name
        self.age = age
        self.salary = salary
    
    def getInfo(self):
        print(f"Programmer name is {self.name}. programmer age and salary is {self.age}, {self.salary}")

p1 = Programmer("Alpha", 25, 200000)
p2 = Programmer("Bravo", 26, 300000)
p3 = Programmer("Charlie", 27, 400000)

p1.getInfo()


# 2..
import math

class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3

    def square_root(self):
        return math.sqrt(self.num)


c = Calculator(4)
print("Square:", c.square())
print("Cube:", c.cube())
print("Square Root:", c.square_root())


# 3..
class Test:
    a = 5   # class attribute

obj = Test()
obj.a = 0   # instance attribute

print("Object a:", obj.a)
print("Class a:", Test.a)


# 4..
import math

class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3

    def square_root(self):
        return math.sqrt(self.num)

    @staticmethod
    def greet():
        print("Hello User!")


c = Calculator(9)
c.greet()


# 5..
class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def get_status(self):
        print(f"Available seats: {self.seats}")

    def get_fare(self):
        print(f"Ticket fare: Rs {self.fare}")

    def book_ticket(self):
        if self.seats > 0:
            print("Ticket booked successfully!")
            self.seats -= 1
        else:
            print("No seats available")


t = Train("Rajdhani Express", 2, 1500)

t.get_status()
t.book_ticket()
t.book_ticket()
t.book_ticket()
t.get_status()


# 6..
class Demo:
    def __init__(harry, name):
        harry.name = name

    def show(harry):
        print("Name is:", harry.name)


d = Demo("Alex")
d.show()