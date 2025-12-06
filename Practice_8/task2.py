import re
import math
s = input("Input a b c:")

try:
    p = r'^[\d\s-]+$'
    if not re.search(p, s):
        raise ValueError('Input datais invalid')
    a, b, c = map(int, s.split())
    D = b*b - 4* a*c 
    x1 = ((-1)* b + math.sqrt(D))/(2*a)
    x2 = ((-1)* b - math.sqrt(D))/(2*a)
except ValueError as e:
    print(e)
    print("Try to enter data so that it would be possible to solve it")
except ZeroDivisionError as zr:
    print(zr)
    print("Try to avoid division by zero")
else:
    print("Roots of the equation",x1,x2)
