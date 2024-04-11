with open("files/6_a.txt") as f:
    n = int(f.readline())
    sp = map(int, f.readlines())

t = [0] * 83
for i in sp:
    t[i % 83] += 1
s = t[0] * (t[0] - 1) // 2
for i in range(1, 42):
    s += t[i] * t[83 - i]
print(s)