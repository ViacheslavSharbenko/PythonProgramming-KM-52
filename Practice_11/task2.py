# ВАШ КОД ТУТ
def rrange(begin,end,step=1):
    if (begin > end and step >=0) or (begin < end and step <=0):
        return []
    if begin < end:
        if begin == end-1:
            return [end-1]
    else: 
        if begin == end+1:
            return [end+1]
    return [begin, *rrange(begin+step, end, step)]
# ПЕРЕВІРКА
x = rrange(1, 10)
y = rrange(10, 1, -1)
z = rrange(10, 1, 1)
print(x, y, z)
assert x == list(range(1, 10)), 'Failed test for simple range'
assert y == list(range(10, 1, -1)), 'Failed test for reverse range'
assert z == list(range(10, 1, 1)), 'Failed test for empty range'
print('All tests good!')