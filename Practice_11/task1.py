# ВАШ КОД ТУТ
def cons(head,tail =[]):
    result = [head]
    for i in tail:
        result.append(i)
    return result




# ПЕРЕВІРКА
l = cons(3, 
        cons(2, 
            cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')



# ВАШ КОД ТУТ

def sum(lst, n= -100):
    if n == -100:
        n = len(lst)
    if n == 1:
        return lst[0]
    return lst[n-1] + sum(lst, n-1)




# ПЕРЕВІРКА
print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')

