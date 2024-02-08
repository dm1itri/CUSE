"""https://education.yandex.ru/ege/task/7ccbf895-92ee-408c-a5ed-f93ff028a916"""


def func(i):
    i = list(map(int, i.split())) + [0]
    return i[1] + i[2] + max(i[3], i[4]), i[0]


with open("applicants1.txt", "r") as f:
    f.readline()
    sp = sorted(map(func, f.readlines()), reverse=True)

print(sp[99])
print([i for i in sp if i[1]][96])
