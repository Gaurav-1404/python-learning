l = [1, 2, 3, 4, 5]
square = lambda x: x*x
# map(function, input_list)       # the function can be lambda function 
sqList = map(square, l)
print(list(sqList))


# list(filter(function, list))     # the function can be lambda function 

def even(n):
    if(n%2 == 0):
        return True
    return False
onlyEven = filter(even,l)
print(list(onlyEven))


from functools import reduce 
# val=reduce (function, list1)    # the function can be lambda function 

def sum(a, b):
    return a + b

print(reduce(sum, l))
