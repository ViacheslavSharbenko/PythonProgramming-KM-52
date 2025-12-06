s1 = input("Enter Phrase1:").lower()
s2 = input("Enter Phrase2:").lower()
l1 = []
l2 = []
for i in s1:
    if i.isalpha():
        l1.append(i)
for i in s2:
    if i.isalpha():
        l2.append(i)
l1 = set(l1)
l2 = set(l2)
print("Phrase1 letters:", l1)
print("Phrase2 letters:", l2)
if l2.issubset(l1):
    print("Yes, with letters from phrase1 it is possible to build phrase 2")
else: 
    print("No, with letters from phrase1 it is impossible to build phrase 2")