class A:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attributes of a is: {cls.a}")

    @property
    def name(self):
        return "{self.fname} {self.lname}"

    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

a1 = A()
a1.a = 30
a1.show()

a1.name = "Alex Devine"
print(a1.fname, a1.lname)