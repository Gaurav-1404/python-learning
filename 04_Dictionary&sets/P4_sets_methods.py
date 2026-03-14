'''
Method	    Description

add()	    Adds an element to the set
update()	Adds multiple elements
remove()	Removes an element
discard()	Removes element without error
pop()	    Removes a random element
clear()	    Removes all elements
copy()	    Returns a copy of the set
union()	    Combines two sets
intersection()	    Returns common elements
difference()	    Returns elements in first set but not second
symmetric_difference()	    Returns elements not common in both
'''
s = {1,2,3}
# add function
s.add(4)
print(s)

# update function
s.update([2,4,6,9,11])
print(s)

# remove function
s.remove(2)
print(s)

# discard function
s.discard(7) 

# pop function
s.pop()
print(s)

# union function
s1 = {2,7,13}
print(s.union(s1))

# Intersection function
a = {1,2,3,4}
b = {2,3,6}
print(a.intersection(b))

# difference function
print(a.difference(b))

