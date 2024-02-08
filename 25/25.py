"""Определите количество составных натуральных чисел из диапазона [2; 20000], у которых количество
 простых собственных делителей больше трех."""

from sympy import primerange

count_all = 0
for i in range(2, 20001):
    count = 0
    for j in primerange(1, i // 2 + 1):
        if i % j == 0:
            count += 1
    count_all += count > 3
print(count_all)
