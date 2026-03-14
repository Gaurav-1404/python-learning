# creation on dictionary
ab = {} # empty dictioary
a = {
    "key" : "value",
    "Alex" : "code",
    "marks" : "100",
    "list" : [1, 2, 9]
}
print(a["key"])      # Output: "value" 
print(a["list"])     # Output: [1, 2, 9] 
print(a["marks"])    # Output: 100

marks = {
    "Alpha" : 10,
    "Bravo" : 9,
    "charlie" : 7,
    "delta" : 10
}
print(marks, type(marks))
print(marks["Alpha"])

print(len(a))

# user input in dict
student = {"name" : "Marks"}
for i in range(4):
    name = input("Enter studnet name: ")
    marks = input("Enter marks: ")
    student[name] = marks
print(student)
