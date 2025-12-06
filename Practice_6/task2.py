s = input("Enter you word(s):").lower()
points = {("a","e","i","l","n","o","r","s","t",'u') : 1,
           ("d", "g") : 2, ("b", "c", "m", "p") : 3,
             ("f","h","v","w","y"): 4, ("k"):5, ("j", "x") : 8,
               ("q", "z"): 10 }
a = 0
for i in s:
    if i.isalpha():
        for j in points:
            if i in j:
                a += points[j] 
    elif a != 0:
        print(a,end=" ")
        a = 0
if a > 0:
    print(a)

