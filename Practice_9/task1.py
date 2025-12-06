import numpy as np
import itertools

def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

#Example of using permutations() method
def input_integer_number():
    """Asking to enter a positive integer number untill it is written correctly"""
    a = 12.5
    while a != int(a) or a <=0 :
        a = input("Enter a positive integer number:")
        if set(a).issubset({"1","2","3","4","5","6","7","8","9","0"}):
            a = int(a)
        else:
            a = 12.5
            continue
    return a

def permutation_list_generation(p):
    """Generating all permutations with indexes from 0 to p-1"""
    l =  [i for i in range(p)]
    return list(itertools.permutations(l, p))
def count_inversions(l):
    """count inversions in list/tuple of integers"""
    r = 0
    for i in range(len(l)-1):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                r+= 1
    return r

def products(m, list_of_permutations):
    """For each permutation counts a sign and a value so that first indexes are 0,1,2... and second are elements os current permutation"""
    result = []
    for i in list_of_permutations:
        sign = count_inversions(i)
        if sign % 2 ==0:
            sign = 1
        else:
            sign = -1
        pr= sign
        for j in range(len(m)):
            pr*= m[j][i[j]]
        result.append(pr)
    return result

def s(list_of_products):
    """calculating a sum of digits in a list/tuple"""
    sm = 0
    for i in list_of_products:
        sm+= i
    return sm
        
n =  input_integer_number()
m = random_matrix(n)
print(m)
permutations = permutation_list_generation(n)
print(s(products(m, permutations)))
print(np.linalg.det(m))




