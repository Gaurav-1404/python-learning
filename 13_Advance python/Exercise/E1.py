# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same. 
files = ["1.txt", "2.txt", "3.txt"]

for file in files:
    try:
        f = open(file, "r")
        print(f"{file} opened successfully.")
        f.close()
    except FileNotFoundError:
        print(f"{file} is not present. Please create it.")

