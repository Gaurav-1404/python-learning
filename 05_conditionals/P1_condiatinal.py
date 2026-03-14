# if, elif and else

print("Check the grade based on marks")

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F (Fail)")

print("Enter two numbers to compare:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Reational operators
print("\nRelational Operators")

if a == b:
    print("a is equal to b")

if a >= b:
    print("a is greater than or equal to b")

if a <= b:
    print("a is less than or equal to b")

# Logical Operators
print("\nLogical Operators Example")

x = int(input("Enter marks in subject 1: "))
y = int(input("Enter marks in subject 2: "))

# and operator
if x >= 40 and y >= 40:
    print("You passed both subjects")
else:
    print("You failed in at least one subject")

# or operator
if x >= 40 or y >= 40:
    print("You passed in at least one subject")
else:
    print("You failed both subjects")

# not operator
z = int(input("Enter your age: "))

if not (z < 18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")