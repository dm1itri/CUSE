with open("24.txt") as f:
    s = f.readline()
count_5, count = 0, 1
for i in range(1, len(s)):
    if s[i] > s[i - 1]:
        count += 1
    else:
        if count == 5:
            count_5 += 1
        count = 1

print(count_5)
