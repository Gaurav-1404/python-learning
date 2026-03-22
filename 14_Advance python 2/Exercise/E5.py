# 5. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

numbers = [10, 23, 45, 50, 12, 30]

maximum = reduce(lambda a, b: a if a > b else b, numbers)

print(maximum)