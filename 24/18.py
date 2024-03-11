with open("18.txt") as f:
    s = f.readline()
max_count = count = 1

for i in range(1, len(s)):
    if s[i - 1] in ("N", "O", "P") and s[i] in ("N", "O", "P"):
        count = 1
    else:
        count += 1
    max_count = max(max_count, count)
print(max_count)
