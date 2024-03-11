"""Текстовый файл состоит из символов A, C, D, F, О. Определите максимальное количество идущих подряд пар символов вида
согласная + согласная + гласная"""

with open("19.txt") as f:
    s = f.readline()
sogl = 0
max_count = count = 0
for i in s:
    if sogl in (0, 1):
        if i in ("C", "D", "F"):
            sogl += 1
        else:
            sogl = min(sogl + 1, 1)
            count = 0
    else:
        if i in ("A", "O"):
            sogl = 0
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
print(max_count)
