"""Текстовый файл состоит из символов A, B, C, D, E, F и G. Определите в прилагаемом файле
минимальное количество идущих подряд символов (длину непрерывной подпоследовательности),
среди которых символ А встречается не менее 500 раз."""

with open("32.txt") as f:
    s = f.readline()

sp = [i for i in range(len(s)) if s[i] == "A"]
min_len = 10**9
for i in range(499, len(sp)):
    min_len = min(min_len, sp[i] - sp[i - 499] + 1)
print(min_len)
