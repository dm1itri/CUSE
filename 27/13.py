with open("files/13_b.txt") as f:
    f.readline()
    sp = map(int, f.readlines())

t = [10**9] * 93
res = 10**9
for i in sp:
    t[i % 93] = min(t[i % 93], i)
for i in range(1, 47):
    res = min(res, t[i] + t[93 - i])
print(res)