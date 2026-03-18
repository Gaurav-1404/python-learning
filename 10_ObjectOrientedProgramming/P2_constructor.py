class Employee:
    def __init__(self):
        print("Good evening")
    def __init__(self, name, age, salary): # dunder method which is automatically called
        print("I am creating an object")
        self.name = name
        self.salary = salary
        self.age = age

    def getInfo(self):
        print(self.name, self.age, self.salary)

    

emp1 = Employee("Alex", 23, 2000000)
emp1.getInfo()
