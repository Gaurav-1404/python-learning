"""
1. Write a python program to display a user entered name followed by Good 
    Afternoon using input () function. 
2. Write a program to fill in a letter template given below with name and date. 
    letter = '''  
    Dear <|Name|>, 
    You are selected! 
    <|Date|> 
    ''' 
3. Write a program to detect double space in a string. 
4. Replace the double space from problem 3 with single spaces. 
5. Write a program to format the following letter using escape sequence 
    characters. 
    letter = "Dear Harry, this python course is nice. Thanks!" 
"""

# 1.. 
name = input("Enter your name: ")
print("Good afternoon!", name)

# 2..
date = input("Enter date (dd/mm/yyyy): ")
print("Dear:" , name ,"\n You are selected!\n ",date)

# 3..
text = " Python is  a powerfull language"
if"  " in text:
    print("Double space found.")
else:
    print("duble space not found.")

# 4..
if"  " in text:
    print("Double space found.\nNow string is:",text.replace("  " , "   "))

else:
    print("duble space not found.")

# 5..
letter = "Dear Alex,\nThis Python course is nice.\nThanks!"
print(letter)