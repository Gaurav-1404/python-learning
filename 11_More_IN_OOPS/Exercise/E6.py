# 6.. Write __str__() method to print the vector as follows: 7i + 8j +10k  
class Vector:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        result = ""
        unit = ['i', 'j', 'k', 'l', 'm']  # for higher dimensions

        for i in range(len(self.values)):
            result += f"{self.values[i]}{unit[i]} + "
        
        return result[:-3]   # remove last ' + '


v = Vector([7, 8, 10])
print(v)

#
