"""Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [258274;
258297], числа, имеющие ровно два различных натуральных делителя, не считая единицы и самого
числа. Для каждого найденного числа запишите эти два делителя в таблицу на экране с новой строки
в порядке возрастания произведения этих двух делителей. Делители в строке таблицы также должны
следовать в порядке возрастания. Например, в диапазоне [5; 9] ровно два целых различных
натуральных делителя имеют числа 6 и 8, поэтому для этого диапазона таблица на экране должна
содержать следующие значения: 2 3 2 4"""


for i in range(258274, 258297):
    sp = set()
    for d in range(2, int(i ** 0.5) + 1):
        if i % d == 0:
            sp.add(d)
            sp.add(i // d)
    if len(sp) == 2:
        print(min(sp), max(sp))