with open("files/10_a.txt") as f:
    f.readline()
    sp = map(int, f.readlines())

t = [0] * 10
res = c_1 = c_2 = c_5 = c_10 = 0
for i in sp:
    res += t[(10 - i % 10) % 10]
    t[i % 10] += 1
print(res)