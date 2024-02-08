# https://education.yandex.ru/ege/task/0b238aec-7379-4f95-b28f-a6c1cbfc18c4


with open("2.txt") as f:
    s = f.readline().replace("CSGO", "    ").replace("PC", "  ")
max_count = count = 0
for i in s:
    if i.isalpha():
        count = -1
    count += 1
    max_count = max(count, max_count)
print(max_count)
