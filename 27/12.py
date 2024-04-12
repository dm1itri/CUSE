with open("files/12_b.txt") as f:
    f.readline()
    sp = map(int, f.readlines())
t = [0] * 91
res = 0
for i in sp:
    res += t[(91 - i % 91) % 91]
    t[i % 91] += 1
print(res)