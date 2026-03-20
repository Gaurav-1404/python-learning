# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt. 
num = int(input("Enter the number which you want table: "))
with open("tables.txt", "w") as f:
    for i in range (1,11):
        f.write(f"{num} x {i} = {num*i}\n")