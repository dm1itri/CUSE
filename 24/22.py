"""

В текстовом файле находится цепочка из прописных (заглавных) символов латинского алфавита A, B, C, D, E, F. Найдите количество подцепочек из трех символов, в которых символы идут не в убывающем алфавитном порядке и индекс первой буквы последней найденной подцепочки (первый символ исходной цепочки имеет индекс 0).
Например, у цепочки ABCFF таких подцепочек три: ABC, BCF и CFF, а индекс первой буквы последней найденной подцепочки (CFF) два и, следовательно, ответ: 3 2.
Отсчёт идет с нуля
"""

with open("22.txt") as f:
    s = f.readline()
count = 0
for i in range(2, len(s)):
    if s[i] >= s[i - 1] >= s[i - 2]:
        count += 1
        index = i - 2
print(count, index)
