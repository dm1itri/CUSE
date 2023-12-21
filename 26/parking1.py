'''https://education.yandex.ru/ege/task/15e49bb8-3179-465b-baaa-e11efdd21bf0'''
from operator import itemgetter


def func(i):
    i = i.split()
    return int(i[0]), int(i[0]) + int(i[1]), i[2] == 'B'


with open('parking1.txt') as f:
    n = int(f.readline())
    sp = sorted(map(func, f.readlines()))

count_bus = count_skip = 0

parking_lot_bus = [None] * 30
parking_lot = [None] * 70
for i in sp:
    parked = False
    if not i[2]:
        for j in range(70):
            if parking_lot[j] == None or parking_lot[j][1] <= i[0]:
                parking_lot[j] = i
                parked = True
                break
    if not parked or i[2]:
        for j in range(30):
            if parking_lot_bus[j] == None or parking_lot_bus[j][1] <= i[0]:
                parking_lot_bus[j] = i
                parked = True
                break
        if not parked:
            count_skip += 1
    if parked and i[2]:
        count_bus += 1

print(count_bus, count_skip)

