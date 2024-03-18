with open("27.txt") as f:
    sp = f.readlines()
count = 0
for i in sp:
    if i.count("R") < 30:
        for j in range(2, len(i)):
            if i[j - 2] == i[j] and i[j] != i[j - 1]:
                count += 1
print(count)
