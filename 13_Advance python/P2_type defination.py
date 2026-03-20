from typing import List, Tuple, Dict, Union
# Type hint
numbers : List[int] = [1, 2, 3, 4]

person : Tuple[str, int] = ["Hello", 23]

identifier : Union[str,int] = "A12BN16"

print(person)
print(type(identifier))


n : int = 5

name : str = "Alex"

def sum(a : int ,b : int) ->int:
    return a+b

print(sum(5,7))