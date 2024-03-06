"""Текстовый файл 24_4.txt состоит не более чем из 120000 символов P, Q. S, и R. Определите
максимальное количество идущих подряд символов, среди которых нет Q, стоящих рядом. Для
выполнения этого задания следует написать программу."""

with open("14.txt") as f:
    s = f.readline()
max_len = curr_len = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1] == "Q":
        curr_len = 1
    else:
        curr_len += 1
    max_len = max(max_len, curr_len)
print(max_len)
