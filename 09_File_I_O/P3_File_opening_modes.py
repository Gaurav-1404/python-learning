# Python File Opening Modes - Complete Demo

# r → Read mode (default)
try:
    f = open("file.txt", "r")
    print("Read mode (r):")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("file.txt not found for read mode")


# w → Write mode (overwrites file)
f = open("file.txt", "w")
f.write("This is write mode (w)\n")
f.close()
print("Write mode (w): File overwritten")


# a → Append mode (adds data at end)
f = open("file.txt", "a")
f.write("This line is added using append mode (a)\n")
f.close()
print("Append mode (a): Data added")


# x → Create mode (creates new file, error if exists)
try:
    f = open("newfile.txt", "x")
    f.write("This file is created using x mode\n")
    f.close()
    print("Create mode (x): File created")
except FileExistsError:
    print("newfile.txt already exists")


# rb → Read binary mode
try:
    f = open("file.txt", "rb")
    print("Read binary mode (rb):")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("file.txt not found for binary read")


# wb → Write binary mode
f = open("binaryfile.bin", "wb")
f.write(b"Binary data example")
f.close()
print("Write binary mode (wb): Binary data written")


# r+ → Read and write mode
try:
    f = open("file.txt", "r+")
    print("r+ mode (read + write):")
    print(f.read())
    f.write("\nAdded using r+ mode")
    f.close()
except FileNotFoundError:
    print("file.txt not found for r+ mode")


# w+ → Write + Read (overwrites)
f = open("file.txt", "w+")
f.write("Using w+ mode\n")
f.seek(0)
print("w+ mode content:")
print(f.read())
f.close()


# a+ → Append + Read
f = open("file.txt", "a+")
f.write("Using a+ mode\n")
f.seek(0)
print("a+ mode content:")
print(f.read())
f.close()


print("File modes demo completed!")