a = int(input("Enter the amount of minutes:"))
def func(n):
    if n<= 50:
        return 100
    if n <=100:
        return 150 
    return 150 + 2*(n-100)


print(func(a))
