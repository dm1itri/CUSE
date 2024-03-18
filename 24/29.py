with open("29.txt") as f:
    s = f.readline()
min_len = 10**9
sp = [i for i in range(len(s)) if s[i] == "A"]
print(min(sp[i] - sp[i - 34] + 1 for i in range(34, len(sp))))
