class Number:
    def __init__(self,n):
        self.n = n
    def __add__(self, num):
        return self.n + num.n
    def __sub__(self, num):
        return self.n - num.n
    def __mul__(self, num):
        return self.n * num.n
    def __truediv__(self, num):
        return self.n / num.n
    def __floordiv__(self, num):
        return self.n // num.n
    
class Name:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"{self.name}"
    
    def __len__(self):
        return len(self.name)
    

n = Number(1)
m = Number(2)


print( n + m )
print( n - m )
print( n * m )
print( n / m )
print( n // m)

n1 = Name("Gaurav")
print(len(n1))

