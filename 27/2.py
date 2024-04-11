with open("files/2_b.txt") as f:
    n = int(f.readline())
    sp = map(int, f.readlines())
t = [0] * 12
for i in sp:
    t[i % 12] += 1

s = t[0] * (t[0] - 1) // 2 + t[6] * (t[6] - 1) // 2
for i in range(1, 6):
    s += t[i] * t[12-i]
print(s)