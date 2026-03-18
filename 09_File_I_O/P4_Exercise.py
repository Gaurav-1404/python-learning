'''
1. Write a program to read the text from a given file ‘poems.txt’ and find out 
    whether it contains the word ‘twinkle’. 
2. The game() function in a program lets a user play a game and returns the score 
    as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
    contains the previous Hi-score. You need to write a program to update the Hi
    score whenever the game() function breaks the Hi-score. 
3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
    different files. Place these files in a folder for a 13 – year old. 
4. A file contains a word “Donkey” multiple times. You need to write a program 
    which replace this word with ##### by updating the same file.  
5. Repeat program 4 for a list of such words to be censored. 
6. Write a program to mine a log file and find out whether it contains ‘python’. 
7. Write a program to find out the line number where python is present from ques 6. 
8. Write a program to make a copy of a text file “this. txt” 
9. Write a program to find out whether a file is identical & matches the content of 
    another file. 
10. Write a program to wipe out the content of a file using python. 
11. Write a python program to rename a file to “renamed_by_ python.txt.
'''
# 1..
f = open("Poems.txt")
poem = f.read().lower()
if "twinkle" in poem:
    print("It contains 'twinkle' ")
else:
    print("It does not contains 'twinkle' ")
f.close()


# 2..
def game():
    # Example: return some score (you can replace with actual game logic)
    return int(input("Enter your score: "))
score = game()

# Read previous hi-score
try:
    with open("Hi-score.txt", "r") as f:
        data = f.read()
        if data == "":
            hi_score = 0
        else:
            hi_score = int(data)
except FileNotFoundError:
    hi_score = 0

# Compare and update
if score > hi_score:
    with open("Hi-score.txt", "w") as f:
        f.write(str(score))
    print("New Hi-score updated!")
else:
    print("Score did not beat Hi-score.")

print("Current Hi-score:", max(score, hi_score))


# 3..
import os
# Folder name
folder_name = "Tables_for_13_year_old"

# Create folder (if not exists)
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Generate tables from 2 to 20
for i in range(2, 21):
    file_path = f"{folder_name}/table_of_{i}.txt"
    
    with open(file_path, "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}\n")

print("All tables created successfully!")


# 4..
try:
    with open("file.txt","r") as f:
        text = f.read().lower()
        text = text.replace("donkey","#####")
        with open("file.txt","w") as f:
            f.write(text)
except FileNotFoundError:
    print("File not found")


# 5..
words = ["donkey", "bad", "ugly"]
try:
    with open("file.txt","r") as f:
        text = f.read().lower()

        for word in words:
            text = text.replace(word , "#####")
        
    with open("file.txt", "w") as f:
        f.write(text)
    print("Censoring completed")

except FileNotFoundError:
    print("File not found!")


# 6..
try:
    with open("file.txt" , "r") as f:
        content = f.read().lower()
    
    if "python" in content:
        print("Yes, 'python' is present in the log file.")
    else:
        print("No, 'python' is not present in the log file.")
except FileNotFoundError:
    print("Log file not found")


# 7..
try:
    with open("log.txt", "r") as f:
        line_no = 1
        found = False

        for line in f:
            if "python" in line.lower():
                print("Python found at line:", line_no)
                found = True
            line_no += 1

        if not found:
            print("Python not found in file")

except FileNotFoundError:
    print("Log file not found")


# 8..
try:
    with open("text.file", "r") as f:
        text = f.read()
    
    with open("copyThis.txt","x") as f:
        f.write(text)

except FileNotFoundError:
    print("File not found")


# 9..
try:
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
        data1 = f1.read()
        data2 = f2.read()

    if data1 == data2:
        print("Both files are identical")
    else:
        print("Files are different")

except FileNotFoundError:
    print("One or both files not found")


# 10..
try:
    with open("file.txt", "w") as f:
        pass   # do nothing, file gets emptied

    print("File content wiped successfully!")

except FileNotFoundError:
    print("File not found")


# 11..
import os

try:
    os.rename("file.txt", "renamed_by_python.txt")
    print("File renamed successfully!")

except FileNotFoundError:
    print("File not found")

except FileExistsError:
    print("A file with new name already exists")