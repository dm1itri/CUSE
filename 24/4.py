"""Текстовый файл 24-1.txt состоит из символов латинского алфавита. Определите максимальное
количество идущих подряд символов, среди которых каждые два соседних различны."""
with open('4.txt') as f:
    s = f.readline()
curr_len = max_len = 1
for i in range(1, len(s)):
    curr_len = 1 + curr_len * (s[i] != s[i-1])
    max_len = max(max_len, curr_len)
print(max_len)
