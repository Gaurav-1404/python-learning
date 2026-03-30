# 2. Write a program to print third, fifth and seventh element from a list using enumerate function. 
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for index, value in enumerate(l):
    if index in [3, 5, 7]:
        print(value)