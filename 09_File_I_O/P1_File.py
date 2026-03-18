f = open("python-learning/09_File_I_O/file.txt") #by defualt r mode 
data = f.read()
print(data)
f.close()

with open("python-learning/09_File_I_O/file.txt") as f:
    data = f.read()
    print(data)

f = open("python-learning/09_File_I_O/file.txt", "w")
f.write("Good evening!")
f.close()