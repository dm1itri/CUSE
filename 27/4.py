with open("files/4_a.txt") as f:
    n = int(f.readline())
    sp = map(int, f.readlines())

t = [0] * 3
for i in sp:
    if i % 26 == 0:
        t[2] += 1
    elif i % 13 == 0:
        t[1] += 1
    elif i % 2 == 0:
        t[0] += 1
print(n*(n - 1) // 2 - (t[2] * (n - t[2]) + t[2] * (t[2] - 1) // 2 + t[1] * t[0]))