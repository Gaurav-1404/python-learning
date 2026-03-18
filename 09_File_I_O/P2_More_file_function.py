# Python File Handling - Complete Guide

# 1. Opening a file
f = open("python-learning/09_File_I_O/file.txt", "r")
print("File opened in read mode")
f.close()


# 2. Reading a file
# Read full content
with open("file.txt", "r") as f:
    print("Full content:")
    print(f.read())

# Read first 5 characters
with open("file.txt", "r") as f:
    print("First 5 characters:", f.read(5))

# Read line by line
with open("file.txt", "r") as f:
    print("First line:", f.readline())
    print("Second line:", f.readline())

# Read all lines as list
with open("file.txt", "r") as f:
    print("All lines:", f.readlines())


# 3. Writing to a file (overwrite mode)
with open("file.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Python File Handling\n")


# 4. Writing multiple lines
with open("file.txt", "w") as f:
    f.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])


# 5. Appending to a file
with open("file.txt", "a") as f:
    f.write("This is appended line\n")


# 6. tell() and seek()
with open("file.txt", "r") as f:
    print("Current position:", f.tell())
    f.seek(5)
    print("After seek(5):", f.read())


# 7. flush()
f = open("file.txt", "w")
f.write("Flushing example")
f.flush()
f.close()


# 8. Exception Handling
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")


print("File handling demo completed!")


f = open("python-learning/09_File_I_O/file2.txt")

# data = f.readlines()
# print(data)

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()

f = open("python-learning/09_File_I_O/file2.txt", "a")
f.write("\nGood evening!")
f.writable()
print(f.tell())
f.close()