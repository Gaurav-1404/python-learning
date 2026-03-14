'''
Method	    Description

get()	    Returns value of a key
keys()	    Returns all keys
values()	Returns all values
items()	    Returns key-value pairs
update()	Updates dictionary with another dictionary
pop()	    Removes a key and returns its value
popitem()	Removes the last inserted key-value pair
copy()	    Returns a copy of the dictionary
clear()	    Removes all elements from dictionary
setdefault()	Returns value of a key, if not present inserts key
'''
Student = {
    "name" : "Alex",
    "age"  :  25
}
# get fuction
print(Student.get("name"))

# keys function
print(Student.keys())

# values function
print(Student.values())

# items function
print(Student.items())

# update function
Student.update({"city" : "noida"})
print(Student.items())

# pop function
print(Student.pop("age"))
print(Student)

# popitem function
print(Student.popitem())
print(Student)

Student.update({"age" : 28,
                "city" : "meerut"})
print(Student)
# copy function
new_dict = Student.copy()
print(new_dict)

# clear function
Student.clear()
print(Student)

# setdefult function
Student.setdefault("age" , 26)
print(Student)
