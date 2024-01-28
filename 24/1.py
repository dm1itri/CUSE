# https://education.yandex.ru/ege/task/a7163d8c-5f01-4b58-a854-e672b5b61d2f
with open('1.txt') as f:
    s = f.readline()
s = s.replace('EA', '  ').replace('NPC', '   ')
max_count = count = 0

for i in s:
    if i.isalpha():
        count = -1
    count += 1
    max_count = max(max_count, count)
print(max_count)

