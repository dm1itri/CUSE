"""Текстовый файл 24-1.txt состоит не более чем из 106 символов. Сколько раз встречается в файле
комбинация «KOT»?"""


with open("7.txt") as f:
    print(f.readline().count("KOT"))