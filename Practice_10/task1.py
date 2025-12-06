import functools
salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
new_salary = list(map(lambda n: round(n*1.3, 2), salary_list))
index_list = list(map(lambda x, y: round(x - y, 2), new_salary, salary_list))
for i in range(len(salary_list)):
    print(salary_list[i], new_salary[i], index_list[i])