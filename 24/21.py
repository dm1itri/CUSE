"""Текстовый файл состоит не более чем из 1 200 000 символов Х, Y, и Z.
Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.
Для выполнения этого задания следует написать программу."""

with open("21.txt") as f:
    s = f.readline().split("XZZY")

print(len(max(s, key=len)) + 6)