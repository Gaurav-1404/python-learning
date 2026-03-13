# Tuple formation
tuple = (1, 3, "ALex", "Run", True, 6)
print("tuple is:", tuple)

# Tuple Methods
numbers = (1, 2, 2, 3)
print(numbers.count(2))


numbers = (10, 20, 30)
print(numbers.index(20))

# SIngle element tuple
Tup1 = (1)
Tup2 = (1,)
print("Tup1 =",Tup1)
print("Tup2 is: ",Tup2)
print("Datatype of tup1", type(Tup1))
print("Datatype of Tup2", type(Tup2))

# Operations with tuples in Python

# Concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6)
result = t1 + t2
print("Concatenation:", result)

# Repetition
t = (1, 2)
print("Repetition:", t * 3)

# Indexing
t = (10, 20, 30, 40)
print("Indexing:", t[1])

# Slicing
t = (10, 20, 30, 40, 50)
print("Slicing:", t[1:4])

# Membership
t = (1, 2, 3)
print("Is 2 in tuple?", 2 in t)

# Length
t = (1, 2, 3, 4)
print("Length:", len(t))

# Minimum and Maximum
t = (5, 2, 9, 1)
print("Minimum:", min(t))
print("Maximum:", max(t))

# Sum
t = (1, 2, 3, 4)
print("Sum:", sum(t))