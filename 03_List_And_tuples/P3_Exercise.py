'''
1. Write a program to store seven fruits in a list entered by the user. 
2. Write a program to accept marks of 6 students and display them in a sorted 
    manner. 
3. Check that a tuple type cannot be changed in python. 
4. Write a program to sum a list with 4 numbers. 
5. Write a program to count the number of zeros in the following tuple: 
    a = (7, 0, 8, 0, 0, 9)
'''
# 1..
print("Enter Seven Fruits name:")
list1 = []
for i in range(0,7):
    list1.append(input())

print(list1)

# 2..
print("Enter the marks:")
List2 = []
for i in range(0,6):
    List2.append(int(input()))
print("Marks:", List2)
List2.sort()
print("Sorted marks:",List2)

# 3..
tup1 = (45,33,55)
print("Orignal Tuple:",tup1)

# t[1] = 50     # give error
print("Tuple after change:", tup1)

# 4..
List3 = [5,6,8,10]
sum = 0
for i in range(0,4):
    sum += List3[i]
print("List is:",List3 )
print("\nSum of the list elements:", sum)

# 5..
a = (7, 0, 8, 0, 0, 9)
print("The number zero occured is:", a.count(0))