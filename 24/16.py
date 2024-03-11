with open("16.txt") as f:
    sp = f.readlines()
count = 0
for i in sp:
    for j in range(2, len(i)):
        if i[j - 2] == "F" and i[j] == "O":
            count += 1
            break
print(count)
