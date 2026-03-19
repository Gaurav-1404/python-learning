class A:
    a = 1
    def show(self):
        print(f"The current value is {self.a}")
    @classmethod
    def show_class_attributes(cls):
        print(f"The class value is {cls.a}")


a1 = A()
a1.a = 45

a1.show()
a1.show_class_attributes()