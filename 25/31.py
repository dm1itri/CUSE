"""Рассматриваются целые числа, принадлежащих числовому отрезку [158928; 345293],
которые представляют собой произведение трёх различных простых делителей. В ответе запишите
количество таких чисел и минимальное из них."""

from sympy import primerange

min_el = 10**6
sp = primerange(345294 // 2)
count = 0
for a in sp:
    for b in sp:
        for c in sp:
            if 158928 <= a * b * c <= 345293 and a < b < c:
                count += 1
                min_el = min(min_el, a * b * c)
print(count, min_el)
