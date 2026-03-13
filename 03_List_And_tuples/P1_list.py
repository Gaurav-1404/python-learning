# List formation
List = ["Rahul", "Alex", 7, True, "Alen", 9]
print("The List is:", List)

# List methods

print("append()")
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

print("\nextend()")
list1 = [1, 2]
list1.extend([3, 4])
print(list1)

print("\ninsert()")
numbers = [1, 3]
numbers.insert(1, 2)
print(numbers)

print("\nremove()")
numbers = [1, 2, 3]
numbers.remove(2)
print(numbers)

print("\npop()")
numbers = [10, 20, 30]
print(numbers.pop(1))
print(numbers)

print("\nclear()")
numbers = [1, 2, 3]
numbers.clear()
print(numbers)

print("\nindex()")
numbers = [10, 20, 30]
print(numbers.index(20))

print("\ncount()")
numbers = [1, 2, 2, 3]
print(numbers.count(2))

print("\nsort()")
numbers = [4, 1, 3, 2]
numbers.sort()
print(numbers)

print("\nreverse()")
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)

print("\ncopy()")
list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)
