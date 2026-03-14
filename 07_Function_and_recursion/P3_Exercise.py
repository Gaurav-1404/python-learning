'''
1. Write a program using functions to find greatest of three numbers. 
2. Write a python program using function to convert Celsius to Fahrenheit. 
3. How do you prevent a python print() function to print a new line at the end. 
4. Write a recursive function to calculate the sum of first n natural numbers. 
5. Write a python function to print first n lines of the following pattern: 
    *** 
    **               
    * - for n = 3 
6. Write a python function which converts inches to cms. 
7. Write a python function to remove a given word from a list ad strip it at the same 
    time. 
8. Write a python function to print multiplication table of a given number.
'''

# 1..
def greatest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else: 
        return num3
print("Enter three numbers to find greatest: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())
great = greatest(num1, num2, num3)
print("The greatest number is:", great)

# 2..
def celToFer(cel):
    return 9*cel/5+32

cel = int(input("Enter celsius temprature: "))
print(celToFer(cel))

# 3..
print("a", end="")
print("b")

# 4..
def SumOfFirstnNumbers(num):
    if(num <= 0):
        return 0
    return num + SumOfFirstnNumbers(num-1)

num = int(input("Enter any number to get first sum of n natural number: "))
print(SumOfFirstnNumbers(num))

# 5..
def pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

pattern(3)

# 6..
def inches_to_cm(inches):
    return inches * 2.54

print(inches_to_cm(5))

# 7..
def remove_and_strip(lst, word):
    new_list = []
    for item in lst:
        item = item.strip()
        if item != word:
            new_list.append(item)
    return new_list

l = ["apple", " banana ", " mango", "grapes ", " banana"]
print(remove_and_strip(l, "banana"))

# 8..
def multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)

multiplication_table(5)