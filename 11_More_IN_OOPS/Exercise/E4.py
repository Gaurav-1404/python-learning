# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded 
#    operators ‘+’ and ‘*’ which adds and multiplies them.
class Complex:
    def __init__(self, a, b ):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} + {self.b}i"
    
    # overloading + operator
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    
    def __mul__(self, other):
        real = self.a * other.a - self.b * other.b
        imag = self.a * other.b + self.b * other.a
        return Complex(real,imag)
    
c1 = Complex(2, 3)
c2 = Complex(4, 5)

print("Addition:", c1 + c2)
print("Multiplication:", c1 * c2)