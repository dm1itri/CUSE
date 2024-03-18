with open("30.txt") as f:
    sp = f.readlines()
min_count, min_s = 10**9, ""
for i in sp:
    if i.count("A") < min_count:
        min_count = i.count("A")
        s = i

max_count = 0
for i in sorted(set(s)):
    if s.count(i) >= max_count:
        max_count = s.count(i)
        symbol = i
print(symbol)
print("".join(sp).count(symbol))
