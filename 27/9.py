with open("files/9_a.txt") as f:
    N = int(f.readline())
    sp = list(map(int, f))

c_1 = c_2 = c_3 = c_6 = 0
res = 0

for i in sp:
    if i % 6 == 0:
        res += c_1 + c_2 + c_3 + c_6
        c_6 += 1
    elif i % 3 == 0:
        res += c_2 + c_6
        c_3 += 1
    elif i % 2 == 0:
        res += c_3 + c_6
        c_2 += 1
    else:
        res += c_6
        c_1 += 1
print(res)