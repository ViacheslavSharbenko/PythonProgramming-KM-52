import math
n = int(input())
def c(n,k):
    return math.factorial(n)/(math.factorial(k)* math.factorial(n-k))
def calculate_binomial_cof(n):
    for i in range(n):
        yield [c(i+1, j) for j in range(0, i+2)]
for i in calculate_binomial_cof(n):
    print(*i)

