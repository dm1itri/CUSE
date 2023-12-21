'''https://education.yandex.ru/ege/task/358d9262-2ade-410e-81e3-62c0790aeeb3'''
with open('2.txt') as f:
    n, m = map(int, f.readline().split())
    sp = sorted((int(i.split()[0]),  int(i.split()[1] != 'Q')) for i in f.readlines())
#  Q == 0

new_sp = []
sp_z = []
m_curr = 0
for i in sp:

    if m_curr + i[0] > m:
        if i[1] == 1:
            continue
        elif m_curr - sp_z[-1][0] + i[0] <= m:
            m_curr += -sp_z[-1][0] + i[0]
            new_sp.remove(sp_z.pop(-1))
            new_sp.append(i)
            continue
        break
    new_sp.append(i)
    m_curr += i[0]
    if i[1]:
        sp_z.append(i)

print(len([i for i in new_sp if i[1] == 0]))
print(m - m_curr)