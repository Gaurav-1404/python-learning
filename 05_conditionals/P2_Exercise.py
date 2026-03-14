'''
1. Write a program to find the greatest of four numbers entered by the user. 
2. Write a program to find out whether a student has passed or failed if it requires a 
    total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
    take marks as an input from the user. 
3. A spam comment is defined as a text containing following keywords: 
    “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
    to detect these spams. 
4. Write a program to find whether a given username contains less than 10 
    characters or not. 
5. Write a program which finds out whether a given name is present in a list or not. 
6. Write a program to calculate the grade of a student from his marks from the 
    following scheme: 
    90 - 100 => Ex 
    80 - 90 => A 
    70 - 80 => B 
    60 - 70  =>C 
    50 - 60 => D 
    <50        
    => F 
7. Write a program to find out whether a given post is talking about “Harry” or not. 
'''
# 1..
print("Question 1: Greatest of Four Numbers")
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

greatest = max(a, b, c, d)
print("Greatest number is:", greatest)


# 2..
print("\nQuestion 2: Pass or Fail")

s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))

total_percentage = (s1 + s2 + s3) / 3

if total_percentage >= 40 and s1 >= 33 and s2 >= 33 and s3 >= 33:
    print("Student Passed")
else:
    print("Student Failed")


# 3..
print("\nQuestion 3: Spam Detection")

message = input("Enter comment: ")

spam_words = ["Make a lot of money", "buy now", "subscribe this", "click this"]

if any(word.lower() in message.lower() for word in spam_words):
    print("This is a spam message")
else:
    print("This is not spam")


# 4..
print("\nQuestion 4: Username Length")

username = input("Enter username: ")

if len(username) < 10:
    print("Username contains less than 10 characters")
else:
    print("Username contains 10 or more characters")


# 5..
print("\nQuestion 5: Name in List")

names = ["Gaurav", "Rahul", "Aman", "Riya"]

name = input("Enter name: ")

if name in names:
    print("Name is present in the list")
else:
    print("Name is not present in the list")


# 6..
print("\nQuestion 6: Grade Calculation")

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade: Ex")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")


# 7. Check if post talks about Harry
print("\nQuestion 7: Check Post")

post = input("Enter post: ")

if "harry" in post.lower():
    print("This post is talking about Harry")
else:
    print("This post is not talking about Harry")