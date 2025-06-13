USER = int(input("enter the number you want to factorial"))

def fact(USER):
    if USER < 2:
        return 1
    else:
        return USER*(fact(USER-1))
k = fact(USER)
print("factorial of given number is",k)