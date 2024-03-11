"""
Текстовый файл состоит из символов G, E и D. Определите максимальное количество подряд идущих троек GDE и GED. Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
"""

with open("20.txt") as f:
    s = f.readline().replace("GDE", "   ").replace("GED", "   ")
count = s[0] == " "
max_count = 0
for i in range(1, len(s)):
    if " " == s[i]:
        count += 1
    else:
        count = 0
    max_count = max(max_count, count / 3)

print(max_count)
