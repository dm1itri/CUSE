'''
Найдите все натуральные числа, N, принадлежащие отрезку [200 000 000; 400 000 000], которые можно представить в виде N = 2𝑚 · 3𝑛, где m – чётное число, n – нечётное число. В ответе запишите все найденные числа в порядке возрастания через пробел.
'''
# from math import log
# print(log(4*10**8, 3))
sp = []
for m in range(0, 29, 2):
    for n in range(1, 19, 2):
        if 2 * 10**8 <= 2 ** m * 3 ** n <= 4 * 10**8:
            sp.append(2 ** m * 3 ** n)
print(*sorted(sp))