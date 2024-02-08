"""https://education.yandex.ru/ege/task/d153be02-c95b-489d-86f0-e9fe7d0b01cf"""

with open("containers1.txt", "r") as f:
    n = int(f.readline())
    sp = sorted(map(int, f.readlines()), reverse=True)

new_sp = [sp.pop(0)]
max_count = 1
for i in sp:
    if i > max(new_sp) - 7:
        new_sp.append(i)
    elif i <= new_sp[0] - 7:
        new_sp[0] = i
        max_count += 1
    else:
        for j in range(1, len(new_sp)):
            if new_sp[j] - 7 >= i:
                new_sp[j] = i
                break
print(new_sp)
print(len(new_sp))
print(max_count)
