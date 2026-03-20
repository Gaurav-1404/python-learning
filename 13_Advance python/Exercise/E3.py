# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.
l = [2, 3, 5, 6, 12, 14, 7, 9, 15, 27, 29, 20]
num = int(input("Enter a number: "))
table = [num * i for i in range(1, 11)]
print(table)

# take out multiple of any number from a given list 
l = [2, 3, 5, 6, 12, 14, 7, 9, 15, 27, 29, 20] 
fl = [i for i in l if (i%3==0)] 
print(fl)