"""https://education.yandex.ru/ege/task/ce678701-0e62-409b-82b7-a5e1946f31c2"""

with open("events1.txt", "r") as f:
    l, n = map(int, f.readline().split())
    sp = [(int(i.split()[0]), int(i.split()[0])) for i in f.readlines()]
