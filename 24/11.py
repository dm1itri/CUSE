"""Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите максимальное
количество идущих подряд символов, среди которых символ Z встречается не более одного раза."""

with open("11.txt") as f:
    sp = f.readline().split("Z")
max_len = 0
for i in range(1, len(sp)):
    max_len = max(max_len, len(sp[i - 1]) + len(sp[i]) + 1)
print(max_len)
