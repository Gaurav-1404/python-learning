''' Exercise 
1. Write a python program to add two numbers. 
2. Write a python program to find remainder when a number is divided by z. 
3. Check the type of variable assigned using input () function. 
4. Use comparison operator to find out whether ‘a’ given variable a is greater than 
    ‘b’ or not. Take a = 34 and b = 80 
5. Write a python program to find an average of two numbers entered by the user. 
6. Write a python program to calculate the square of a number entered by the user. 
'''

# 1..
a = int(input("Enter two numbers: "))
b = int(input())
print("Sum is:" ,a + b)

# 2..
z = 3
print("z =", z)
a = int(input("enter any number to get remainder after devide by z: "))
print(a%z)

# 3..
a = input("Enter something: ")
print("type of the entered variable:", type(a))

# 4..
a = 34
b = 80
print("a =", a)
print("b =", b)
print("Is a greater than b?", a > b)

# 5..
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

average = (n1 + n2) / 2
print("Average:", average)

# 6..
num = int(input("Enter a number: "))
print("Square of the number:", num ** 2)


print("\nAll exercises completed.")