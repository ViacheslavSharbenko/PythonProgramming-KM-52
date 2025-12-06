
def find_max(d):
    m_key = -100000
    m_value = -1000000
    for i in d:
        if d[i] > m_value:
            m_key = i
            m_value = d[i]
    return m_key
most_popular_names = []
for i in range(1880, 2020):
    file = open("yob"+str(i)+".txt", "r+")
    lines = file.readlines()
    m = {}
    f = {}
    for line in lines:
        l = line.split(",")
        if l[1] == "F":
            f[l[0]] = int(l[2])
        else:
            m[l[0]] = int(l[2])
    most_popular_names.append(find_max(m))
    most_popular_names.append(find_max(f))
    file.close()
result = {}
for i in set(most_popular_names):
    result[i] = most_popular_names.count(i)
for i in result:
    print(i," : ", result[i])