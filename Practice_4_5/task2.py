while True:
    r = int(input("Enter score R:"))
    if r>= 0 and r <= 100:
        break
    print("You entered invalid score, i shoud be between 0 and 100, try again")


if r >= 95: 
    print("Excellent")
elif r>= 85:
    print("Very good")
elif r >= 75:
    print("Good")
elif r >= 65:
    print("Satisfactory")
elif r >= 60:
    print("Marginal")
else:
    print("Unsatisfactory")