# using in dry(Don't copy yourself) programming
class Employee:
    company = "Google"
    name = str
    age = int
    salary = int
    def getInfo(self):
        print(f"The company name is {self.company}. the name of employee is {self.name}.")
    @staticmethod
    def greet():
        print("Good evening")

Stu1 = Employee()
Stu1.name = "Alex"
Stu1.age = 18
Stu1.salary = 16000
# Stu1.city = "Agra"  # this is an instance attributes

print(Stu1.name, Stu1.age, Stu1.company, Stu1.salary)

Employee.company = "Facebook"
print(Stu1.company)
print(Stu1.getInfo())

stu2 = Employee()
print(stu2.getInfo())