# Python program demonstrating important string functions

str1 = "harry"

# 1. len() function – returns length of the string
print("Length of string:", len(str1))   # Output: 5

# 2. endswith() – checks if string ends with given word
print("Ends with 'rry':", str1.endswith("rry"))   # Output: True

# 3. count() – counts occurrences of a character
print("Count of 'r':", str1.count("r"))   # Output: 2

# 4. capitalize() – capitalizes the first character
print("Capitalized:", str1.capitalize())   # Output: Harry

# 5. find() – returns index of first occurrence
print("Index of 'rr':", str1.find("rr"))   # Output: 2

# 6. replace() – replaces old word with new word
print("Replace 'harry' with 'Larry':", str1.replace("harry", "Larry"))

text = "hello world"

# 7. upper() – converts string to uppercase
print("Uppercase:", text.upper())

# 8. lower() – converts string to lowercase
print("Lowercase:", text.lower())

# 9. strip() – removes extra spaces
space_text = "  python  "
print("Stripped text:", space_text.strip())

# 10. split() – splits string into a list
sentence = "Python is easy to learn"
print("Split sentence:", sentence.split())