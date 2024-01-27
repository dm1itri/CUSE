"""Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [3954;
8979], числа, имеющие не менее 41 и не более 45 различных делителей. Для каждого найденного числа
запишите сначала это число, а затем количество делителей. Найденные числа из отрезка [3954; 8979]
должны быть указаны в порядке возрастания."""


for i in range(3954, 8979 + 1):
    sp = {1, i}
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            sp.add(j)
            sp.add(i // j)

    if 41 <= len(sp) <= 45:
        print(i, len(sp))