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

n_index = 0
m_index = 0
sum = 0
k = 0

while sum <= s:
    if sum + min(n_list[n_index], m_list[m_index]) > s:
        break

    if n_list[n_index] < m_list[m_index]:
        sum += n_list[n_index]
        k += 1
        if n_index + 1 < n:
            n_index += 1
        continue

    if n_list[n_index] > m_list[m_index]:
        sum += m_list[m_index]  # ??? почему (поменял на m)
        k += 1
        if m_index + 1 < m:
            m_index += 1
        continue

    if n_list[n_index] == m_list[m_index]:
        new_n_index = n_index + 1
        new_m_index = m_index + 1

        while True:
            if n_list[n_index] < m_list[m_index]:
                sum += n_list[n_index]
                k += 1
                if n_index + 1 < n:
                    n_index += 1
                break

            if n_list[new_n_index] > m_list[new_m_index]:
                sum += m[m_index]
                k += 1
                if m_index + 1 < m:
                    m_index += 1
                break

            if new_n_index + 1 < n:
                new_n_index += 1

            if new_m_index + 1 < m:
                new_m_index += 1

print(sum)
print(k)
