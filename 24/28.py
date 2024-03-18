with open("28.txt") as f:
    sp = f.readlines()
count = max_len = 0
for i in sp:
    if i.count("R") < 30:
        for j in range(len(i) - 2):
            for l in range(j + 2, len(i)):
                if i[j] == i[l] and i[j] not in i[j + 1 : l]:
                    count += 1
                    max_len = max(max_len, l - j + 1)
print(max_len, count)
