'''https://education.yandex.ru/ege/task/0cda22ac-3a25-4e88-a66a-01940555d517'''
with open('pits1.txt') as f:
    n = int(f.readline())
    sp = list(map(int, f.readlines()))

new_sp = [sp[0]] + [None] * (n-2) + [sp[-1]]
v = 0
for i in range(1, n-1):
    abc = sp[i-1:i+2]
    new_v = sum(abc) - min(abc) - max(abc)
    new_sp[i] = new_v
    v += max(0, sp[i] - new_v)
print(new_sp.count(min(new_sp)))
print(v)

