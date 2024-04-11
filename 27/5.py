with open("files/5_b.txt") as f:
    n = int(f.readline())
    sp = map(int, f.readlines())
t = [0] * 10
for i in sp:
    t[i % 10] += 1
s = t[0] * (t[0] - 1) // 2 + t[5] * (t[5] - 1) // 2
for i in range(1, 5):
    s += t[i] * t[10-i]
print(s)