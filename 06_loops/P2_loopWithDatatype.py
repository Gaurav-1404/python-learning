# 1. For loop with LIST

fruits = ["apple", "banana", "mango"]

print("Loop through List:")
for fruit in fruits:
    # This loop prints each fruit in the list
    print(fruit)


# 2. For loop with TUPLE

numbers = (10, 20, 30, 40)

print("\nLoop through Tuple:")
for num in numbers:
    # This loop prints each number in the tuple
    print(num)


# 3. For loop with DICTIONARY

student = {
    "name": "Rahul",
    "age": 21,
    "course": "BTech"
}

print("\nLoop through Dictionary Keys:")
for key in student:
    # This prints dictionary keys
    print(key)

print("\nLoop through Dictionary Values:")
for value in student.values():
    # This prints dictionary values
    print(value)

print("\nLoop through Dictionary Key-Value pairs:")
for key, value in student.items():
    # This prints both key and value
    print(key, ":", value)


# 4. For loop with SET

colors = {"red", "blue", "green"}

print("\nLoop through Set:")
for color in colors:
    # This loop prints each color in the set
    print(color)