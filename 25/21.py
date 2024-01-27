"""Напишите программу, которая ищет среди целых чисел больших 900000 первые четыре числа,
имеющие делитель, который оканчивается на 3, но не равен 3. Для каждого найденного числа запишите
это число и минимальный такой делитель."""

count = 0
i = 9 * 10**5
while count < 4:
    i += 1
    sp = set()
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if j % 10 == 3 and j > 10:
                sp.add(j)
            if i // j % 10 == 3:
                sp.add(i // j)
    if sp:
        count += 1
        print(i, min(sp))
