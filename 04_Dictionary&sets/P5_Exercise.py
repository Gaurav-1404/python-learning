''' Questions
1. Write a program to create a dictionary of Hindi words with values as their English 
    translation. Provide user with an option to look it up! 
2. Write a program to input eight numbers from the user and display all the unique 
    numbers (once). 
3. Can we have a set with 18 (int) and '18' (str) as a value in it? 
4. What will be the length of following set s: 
    s = set() 
    s.add(20) 
    s.add(20.0) 
    s.add('20') # length of s after these operations? 
5. s = {} 
    What is the type of 's'? 
6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
    value and use key as their names. Assume that the names are unique. 
7. If the names of 2 friends are same; what will happen to the program in problem 
    6? 
8. If languages of two friends are same; what will happen to the program in problem 
    6? 
9. Can you change the values inside a list which is contained in set S? 
    s = {8, 7, 12, "Harry", [1,2]}
'''
# 1..
print("Question 1: Hindi to English Dictionary")
hindi_dict = {
    "pani": "water",
    "roti": "bread",
    "doodh": "milk",
    "kursi": "chair"
}

word = input("Enter Hindi word: ")
print("Meaning:", hindi_dict.get(word, "Word not found"))


# 2..
print("\nQuestion 2: Unique Numbers")
numbers = set()

for i in range(8):
    n = int(input("Enter number: "))
    numbers.add(n)

print("Unique numbers:", numbers)


# 3..
print("\nQuestion 3")
s = {18, '18'}
print("Set containing 18 and '18':", s)


# 4..
print("\nQuestion 4")
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print("Set:", s)
print("Length of set:", len(s))


# 5..
print("\nQuestion 5")
s = {}
print("Type of s:", type(s))


# 6..
print("\nQuestion 6: Favorite Languages")
fav_lang = {}

for i in range(4):
    name = input("Enter friend's name: ")
    lang = input("Enter favorite language: ")
    fav_lang[name] = lang

print("Favorite Languages Dictionary:", fav_lang)


# 7..
print("\nQuestion 7")
print("If two friends have the same name, the later value will overwrite the previous one.")


# 8..
print("\nQuestion 8")
print("If two friends choose the same language, it will work fine because dictionary values can be the same.")


# 9..
print("\nQuestion 9")
print("A list cannot be stored in a set because lists are mutable.")
print("Example: s = {8, 7, 12, 'Harry', [1,2]} -> This will cause TypeError")