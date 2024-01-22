"""
Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300405.
Среди натуральных чисел, не превышающих 1010, найдите все числа, для которых выполнены все условия:
— соответствуют маске 1?2139*4;
— делятся на 2023 без остатка;
— сумма цифр числа нечётна.
В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце— соответствующие им результаты деления этих чисел на 2023.
"""
from fnmatch import fnmatch


for i in range(0, 10**10, 2023):
    if sum(int(j) for j in str(i)) % 2 and fnmatch(str(i), '1?2139*4'):
        print(i, i // 2023)
