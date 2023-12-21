'''https://education.yandex.ru/ege/task/b2f83157-f7a7-4b97-8e76-11c040aef8a8'''
with open('containers2.txt', 'r') as f:
    n = int(f.readline())
    sp = sorted(map(int, f.readlines()), reverse=True)
print(sp)
max_count = count = 1
for i in range(1, n-1):
    if sp[i] == sp[i-1] - 1:
        count += 1
    else:
        if count >= max_count:
            max_count, min_length = count, sp[i-1]
        count = 1
print(max_count, min_length)

