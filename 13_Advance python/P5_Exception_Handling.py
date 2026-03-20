# try and except block statement
try:
    a = int(input("Hey! Enter any number: "))
    print(a)
except ValueError as v:
    print("Heyy")
    print(v)
except Exception as e:
    print(e)

print("Thankyou!")

# Raise exception
a = int(input("Enter a number: "))
b = int(input("Enter second number: "))
if b == 0:
    raise ZeroDivisionError("program not mean to divide number by 0")
else:
    print(f"The division a/b is {a/b}")


# Try with else
try:
    a = int(input("Enter any number"))
    print(a**a)
except Exception as e:
    print(e)
else:
    print("end")


# try with finally
def main():
    try:
        a = int(input("Enter any number"))
        print(a**a)
    except Exception as e:
        print(e)
    finally:
        print("Programmed successfull")

main()

    

