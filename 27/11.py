with open("files/11_a.txt") as f:
    n = int(f.readline())
    sp = map(int, f.readlines())
res = c_1 = c_2 = c_7 = c_14 = 0
for i in sp:
    if i % 14 == 0:
        res += c_1 + c_2 + c_7 + c_14
        c_14 += 1
    elif i % 7 == 0:
        res += c_2 + c_14
        c_7 += 1
    elif i % 2 == 0:
        res += c_7 + c_14
        c_2 += 1
    else:
        res += c_14
        c_1 += 1
print(n * (n-1) / 2 - res)
