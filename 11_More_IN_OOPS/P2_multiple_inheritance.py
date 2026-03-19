class Employee:
    company = "ITC"
    name = "defualt name"
    salary = 6666
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class coder: 
    language = "python"
    def printLnaguage(self):
        print(f"Out of all other language here is your language: {self.language}")
    
    

class Programmer(Employee, coder):
        company = "ITC Infotech"
        def showLanguage(self):
            print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()


print(a.company, b.company)
b.show()
b.showLanguage()
b.printLnaguage()