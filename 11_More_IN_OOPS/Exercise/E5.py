# problem :5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self, values):
        self.values = values 

    def __str__(self):
        return f"{self.values}"

    # Overloading + operator (vector addition)
    def __add__(self, other):
        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] + other.values[i])
        return Vector(result)

    # Overloading * operator (dot product)
    def __mul__(self, other):
        result = 0
        for i in range(len(self.values)):
            result += self.values[i] * other.values[i]
        return result


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Sum:", v1 + v2)
print("Dot Product:", v1 * v2)