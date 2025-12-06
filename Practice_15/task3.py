from math import *
def check(a,b,c):
    if a > 0 and b > 0 and c >0:
        return True
    return False
def triangle_ineq(func):
    def inner(*args, **kwargs):
        a = args[0]
        b = args[1]
        c = args[2]
        if a > b + c or b> a + c or c > a+ b:
            print("Invalid input data a, b and c must fit triangle inequality")
            return False
        print("Area of the triangle is:",func(*args) )
        return None
    return inner
@triangle_ineq        
def area_calculation(a,b,c):
    if not check(a, b, c):
        print("Invalid input data, sides a, b and c must be positive")
        return False
    p = (a+b+c)/2
    return sqrt(p * (p-a) * (p-b) *  (p-c))
a,b,c = map(int, input().split())
area_calculation(a,b,c)