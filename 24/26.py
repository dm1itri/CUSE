"""Текстовый файл состоит не более чем из 106 заглавных латинских букв (A..Z). Определить и
записать в ответ количество символов самой длинной последовательности, в которой не больше одной
буквы A, а буква B встречается не менее 3 раз. Для выполнения этого задания следует написать
программу."""

with open("26.txt") as f:
    sp = f.readline().split("A")


max_len = 0
for i in range(1, len(sp)):
    if sp[i].count("B") + sp[i - 1].count("B") >= 3:
        max_len = max(len(sp[i]) + len(sp[i - 1]) + 1, max_len)

print(max_len)
