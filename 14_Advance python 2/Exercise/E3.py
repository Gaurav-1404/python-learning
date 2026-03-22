# 3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.
table = [7*i for i in range(1, 11)]

# Convert to vertical string
vertical = "\n".join(str(i) for i in table)

print(vertical)