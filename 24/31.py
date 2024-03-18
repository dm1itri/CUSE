with open("31.txt") as f:
    s = f.readline()
sp = [i for i in range(len(s)) if s[i] == "A"]
min_len = 10**9
for i in range(2023, len(sp)):
    min_len = min(min_len, sp[i] - sp[i - 2023] + 1)
print(min_len)
