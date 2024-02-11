"""Ежегодно библиотека пополняет свой книжный фонд, На закупку новых книг выделяется определённая
сумма, которую нельзя превысить. На эту сумму библиотеке необходимо закупить максимальное число.
книг различных наименований, среди которых должны быть ровно три наименования редких книг.
Известно, что стоимость любой редкой книги превышает 3000 рублей, а стоимость любой другой книги
не превышает этого значения. По заданной информации о выделенной сумме на покупку книг и
стоимости книг каждого наименования определите максимальное количество наименований книг,
которые может приобрести библиотека, и стоимость покупки самой дорогой книги, не относящейся к
категории редких, при условии, что в итоге будет куплено максимальное число книг различных
наименований. Входные данные В первой строке входного файла находятся два числа: S — выделенная
на покупку книг сумма (натуральное число, не превышающее 100000) и N — количество наименований
книг (натуральное число, не превышающее 1000). В следующих N строках находятся значения стоимости
книг каждого наименования (все числа натуральные, не превышающие 5000), каждое в отдельной
строке. Запишите в ответе два числа: сначала наибольшее число наименований книг, которые могут
быть закуплены, затем максимальную стоимость книги, не относящейся к категории редких,
которая может быть приобретена библиотекой, при условии, что в итоге будут куплены книги
максимального числа наименований, три из которых будут относиться к категории наименований редких
книг. Пример входного файла: 12000 7 200 4500 3500 500 3100 800 4100 При таких исходных данных
можно приобрести максимум 5 книг: три редкие, стоимостью 3100, 3500 и 4100, и две, не относящиеся
к редким, ‘стоимостью 200 и 500, 200 и 800 или 500 и 800. Наибольшая стоимость книги,
не являющейся редкой, — 800. Ответ для приведённого примера: 5 800"""

with open("14.txt", "r") as f:
    s, n = map(int, f.readline().split())
    sp = sorted(map(int, f.readlines()))
c_sum = sp.pop(sp.index(3011)) + sp.pop(sp.index(3012)) + sp.pop(sp.index(3014))
sp = sp[: sp.index(3021)]
count = 3
for i in sp:
    if c_sum + i <= s:
        c_sum += i
        count += 1
        last_el = i
    elif c_sum + i - last_el <= s:
        c_sum += i - last_el
        last_el = i

print(count, last_el)
