'''https://education.yandex.ru/ege/task/41f4bd80-aa0d-4458-8484-4eceafb982de'''
with open('satellite_signals.txt') as f:
    n = int(f.readline())
    sp = [tuple(map(int, i.split())) for i in f.readlines()]


longitudes = [0] * 20000
for latitude, longitude in sp:
    longitudes[longitude + 10000] += 1

longitude = longitudes.index(max(longitudes)) - 10000  # longitude = -16,2
print(longitude)
latitudes_162 = set(int(str(i)[0:-1]) for i, j in sp if j == longitude)
print(len(latitudes_162))