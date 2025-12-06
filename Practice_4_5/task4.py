salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
new_salary_list = []
indexation_list = []
for i in salary_list:
    new_salary_list.append(round(i*1.3 , 2))
    indexation_list.append(round(i*0.3, 2))
print("Salary table:")
print(*new_salary_list)
print(*indexation_list)