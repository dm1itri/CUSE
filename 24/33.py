with open("33.txt") as f:
    s = f.readline()

sp = [(i, s[i]) for i in range(len(s)) if s[i] in "AB"]
max_len = 0
for i in range(3, len(sp)):
    if sp[i - 1][1] != sp[i - 2][1]:
        max_len = max(max_len, sp[i][0] - sp[i - 3][0] - 1)
print(max_len)
