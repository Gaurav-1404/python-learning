# 4. Write a program to filter a list of numbers which are divisible by 5.
numbers = [10, 23, 45, 50, 12, 30]

result = list(filter(lambda x: x % 5 == 0, numbers))

print(result)