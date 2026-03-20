myList = [1, 2, 5, 8, 9]
squareList = []
for item in myList:
    squareList.append(item*item)
print(squareList)

# list comprehension
squareList1 = [i*i for i in myList]
print(squareList1)