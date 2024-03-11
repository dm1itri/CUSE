with open("15.txt") as f:
    sp = f.readlines()
count = 0
for i in sp:
    if i.count("E") > i.count("A"):
        count += 1
print(count)
