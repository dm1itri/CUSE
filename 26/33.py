"""Во многих компьютерных системах текущее время хранится в формате «UNIX-время» – количестве
секунд от начала суток 1 января 1970 года. В одной компьютерной системе проводили исследование
загруженности. Для этого в течение месяца с момента UNIX-времени 1633046400 фиксировали и
заносили в базу данных моменты старта и финиша всех процессов, действовавших в этой системе. Вам
необходимо определить, какое наибольшее количество процессов выполнялось в системе одновременно
на неделе, начавшейся в момент UNIX-времени 1634515200, и в течение какого суммарного времени (в
секундах) выполнялось такое наибольшее количество процессов. Входные данные Первая строка
входного файла содержит целое число N – общее количество процессов за весь период наблюдения.
Каждая из следующих N строк содержит 2 целых числа: время старта и время завершения одного
процесса в виде UNIX-времени. Все данные в строках входного файла отделены одним пробелом. Если в
качестве времени старта указан ноль, это означает, что процесс был активен в момент начала
исследования. Если в качестве времени завершения указан ноль, это означает, что процесс не
завершился к моменту окончания исследования. При совпадающем времени считается, что все старты и
завершения процессов происходят одновременно, в начале соответствующей секунды. В частности,
если время старта одного процесса совпадает с временем завершения другого и других стартов и
завершений в этот момент нет, то количество активных процессов в этот момент не изменяется. В
ответе запишите два целых числа: сначала максимальное количество процессов, которые выполнялись
одновременно на неделе, начиная с момента UNIX-времени 1634515200, затем суммарное количество
секунд, в течение которых на этой неделе выполнялось такое максимальное количество процессов."""

with open("33.txt", "r") as f:
    N = int(f.readline())
    sp = [0] * 60 * 60 * 24 * 31
    for i in f.readlines():
        start, end = map(int, i.split())
        sp[max(start - 1633046400, 0)] += 1
        if end:
            sp[end - 1633046400] -= 1
count = 0
max_count = 0
d = 0
for i in range(60 * 60 * 24 * 31):
    count += sp[i]
    i = i
    if 1634515200 - 1633046400 <= i < 1634515200 - 1633046400 + 60 * 60 * 24 * 7:
        if count > max_count:
            max_count = count
            d = 1
        elif count >= max_count:
            d += 1
print(max_count, d)
