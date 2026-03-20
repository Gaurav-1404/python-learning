import random 

ran_num = random.randint(1,100)
user_num = int(input("Enter any number: "))
count = 1

while ran_num != user_num:
    count += 1
    if ran_num < user_num:
        print("“Lower number please")
    else:
        print("higher number please")
    user_num = int(input("Enter again: "))
print("Correct! ")
print("The number of guesses to arrive at number is: ", count)
