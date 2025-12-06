file = open("gadsby.txt", "r+")
lines =  file.readlines()
letters_dict = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
    'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
    'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
    'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
    'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
    'z': 0
}
s = 0
for line in lines:
    for i in line:
        i = i.lower()
        if i in "abcdefghijklmnopqrstuvwxyz":
            letters_dict[i]+=1
            s+=1
dict2 = {}
for i in letters_dict:
    dict2[i] =  round((letters_dict[i]*100 )/s, 3)
    
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]
#На  жаль нічо розумнішого ніж відсортувати бульбашкою не придумав
for i in range(len(letters)):
    for j in range(i, len(letters)):
        if dict2[letters[i]] >  dict2[letters[j]]:
             letters[i], letters[j]= letters[j], letters[i]


file.close()
print ('-----------')
for i in letters[::-1]:
    print(i, " : ", dict2[i])


print("Final answer:")
print("Most used:")
for i in letters[len(letters): len(letters)-6:-1]:
    print(i, " : ", dict2[i])
print("Less used")
for i in letters[4::-1]:

    print(i, " : ", dict2[i])
