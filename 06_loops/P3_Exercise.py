'''
1. Write a program to print multiplication table of a given number using for loop. 
2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
    with S. 
    l = ["Harry", "Soham", "Sachin", "Rahul"] 
3. Attempt problem 1 using while loop. 
4. Write a program to find whether a given number is prime or not. 
5. Write a program to find the sum of first n natural numbers using while loop. 
6. Write a program to calculate the factorial of a given number using for loop. 
7. Write a program to print the following star pattern. 
    * 
    *** 
    ***** for n = 3 
8. Write a program to print the following star pattern: 
    * 
    ** 
    ***      for n = 3 
9. Write a program to print the following star pattern. 
    * * * 
    *   *   for n = 3 
    * * *  
10. Write a program to print multiplication table of n using for loops in reversed 
    order.
'''
# 1..

n = int(input("Enter a number for table: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

# 2..

l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if name.startswith("S"):
        print("Hello", name)

# 3..

num = int(input("Enter a number for table using while loop: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num*i)
    i += 1

# 4..

number = int(input("Enter a number to check prime: "))
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if is_prime and number > 1:
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")

# 5..

n = int(input("Enter n for sum of natural numbers: "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print("Sum =", sum)

# 6..

num = int(input("Enter a number for factorial: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print("Factorial =", factorial)

# 7..

n = 3
for i in range(1, n+1):
    print(" "*(n-i),"*"*(2*i -1),"")

# 8..

n = 3
for i in range(1, n+1):
    print("*" * i)

# 9..
n = 3
for i in range(n):
    if i == 0 or i == n-1:
        print("* " * n)
    else:
        print("*", " "*(2*n-5), "*")

# 10..
n = int(input("Enter number for reverse table: "))
for i in range(10, 0, -1):
    print(n, "x", i, "=", n*i)