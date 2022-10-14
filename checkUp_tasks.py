""" Задача 1. Розыгрыш резюме рьяными работниками"""

# пользовательский ввод
# __________________________________
n, m, s = map(int, input().split())
n_list = []
m_list = []

n_list_increment_of_sum = []
m_list_increment_of_sum = []

for i in range(max(n, m)):
    a, b = map(str, input().split())
    if a != '-':
        n_list.append(int(a))
        n_list_increment_of_sum.append(sum(n_list))
    if b != '-':
        m_list.append(int(b))
        m_list_increment_of_sum.append(sum(m_list))
# __________________________________

print(n_list_increment_of_sum, m_list_increment_of_sum)

# if sum_of_n_list + sum_of_m_list <= s:  # сумма всех зарплат больше s - вернем всю "пачку"
#     print(len(n_list) + len(m_list))
