# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.
class Vector:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        unit = ['i', 'j', 'k', 'l', 'm']
        return " + ".join(f"{val}{unit[i]}" for i, val in enumerate(self.values))

    # Override len()
    def __len__(self):
        return len(self.values)


# Example
v = Vector([1, 2, 3, 4])

print(v)          # vector representation
print(len(v))     # dimension