class Manager:
    company = "Microsoft"

    def __init__(self, name="", project=""):
        self.name = name
        self.project = project

    def projectName(self):
        print(f"{self.name} manager has project '{self.project}' in {self.company}")


class Employee(Manager):
    def __init__(self, emp_name, manager_name, project):
        super().__init__(manager_name, project)   # calling parent constructor
        self.Emp_name = emp_name

    def Emp_data(self):
        print(f"The employee {self.Emp_name} has project '{self.project}' under manager {self.name}")

class Intern(Employee):
    def __init__(self, intern_name, emp_name, manager_name, project, duration):
        super().__init__(emp_name, manager_name, project)
        self.intern_name = intern_name
        self.duration = duration

    def Intern_data(self):
        print(f"Intern {self.intern_name} work with {self.Emp_name} on {self.project} for {self.duration} months under manager {self.name}")

# Manager object
M1 = Manager("Gaurav Gupta", "AI threat detector")
M1.projectName()

# Employee object
E1 = Employee("Alex", "Gaurav Gupta", "AI threat detector")
E1.Emp_data()

I1 = Intern("Ravi", "Alex", "Gaurav Gupta", "'AI threat detector'", 6)
I1.Intern_data()