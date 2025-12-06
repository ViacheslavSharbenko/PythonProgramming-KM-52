items = input("Enter names of the items using space between it:").split(" ")
for i  in range(len(items)):
    if i == len(items) -1  :
        print(items[i],)
    elif i == len(items) - 2:
        print(items[i], "and", end=" ")
    else:
        print(items[i] + ",", end=" ")
