# global variable
a = 89

def fun():
    # global a
    a = 3
    print(a)

fun()
print(a)

# Enumerate function
l = [2, 4, 5, 8, 11]
index = 0
for item in l:
    index += 1
    print(f"The item number {index} is {item}")

# this can be simplified by enumrate function
for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")

    
