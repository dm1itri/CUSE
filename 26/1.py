"""https://education.yandex.ru/ege/task/c5c6b768-42bb-4590-8b90-2317266cc1f2"""

with open("1.txt") as f:
    n = int(f.readline())
    sp = sorted(
        [tuple(map(int, i.split())) for i in f.readlines()], key=lambda x: -x[0]
    )
new_sp = [sp[0]]
for i in sp:
    if i[1] <= new_sp[0][0]:
        new_sp.insert(0, i)

print(len(new_sp))
print(new_sp)
