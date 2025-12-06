import numpy as np

years = np.arange(1900, 2020+5, 1)
def del_years(l, l2):
    r = []
    for i in l:
        if not( i in l2):
            r.append(i)
    return r

def v_years(years):
    v = list(filter(lambda x: x % 400 ==0, years))
    years = del_years(years,v)
    years = del_years(years, list(filter(lambda x: x%100==0,years)))
    v += list(filter(lambda x: x % 4 ==0, years))
    years = del_years(years,v)
    return v
print(v_years(years))
while True:
    month = int(input("Enter the Month:"))
    year_nomber = int(input("Enter the year number:"))
    if month>=1 and month <=12:
        break
    
    
    
    
def count_days(f, month, year):
    if  month==1:
        if year in f(years):
            return 29
        else:
            return 28
    elif month in [4,6,9,11]:
        return 30
    else:
        return 31
print(count_days(v_years,month,year_nomber))
        




