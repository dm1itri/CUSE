with open("files/8_a.txt") as f:
    n = int(f.readline())
    sp = map(int, f.readlines())
t = [[0] * 11 for _ in range(3)]
for i in sp:
    t[2 - i % 3][max(j for j in range(11) if i % 2**j == 0)] += 1
s = t[0][5] * (t[0][5] - 1)//2
for i in range(6, 11):
    s += t[0][i] * sum(t[0][10-i:i]) + t[0][i] * (t[0][i] - 1)//2
s += t[1][5] * t[2][5]
for i in range(11):
    s += t[1][i] * sum(t[2][10-i:])
print(s)