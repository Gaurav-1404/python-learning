# loops in python 
# two types :- 1. for loop    2. while loop

# for loop
print("1 to 10 all numbers")
for i in range(1,11):
    print(i)

print("odd number between 1 to 10")
for i in range(1,11,2):
    print(i)

print("even number between 1 to 10")
i=2

# while loop

while(i<10):
    print(i)
    i += 2

# Break statement
print("numbers from 10 to 5")
while(i>0):
    if(i==5):
        break
    print(i)
    i -=1


# continue statement
print("numbers from 5 to 1 except 2")
while(i>0):
    if(i==2):
        i -= 1
        continue
    print(i)
    i -= 1

# pass statement
for i in range(1,6):
    pass


# loop with else statement
print("Table of 2")
for i in range(1,11):
    print(i*2)
else:
    print("Done!")