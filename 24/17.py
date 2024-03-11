with open("17.txt") as f:
    sp = f.readlines()
count = 0
for i in sp:
    if i.count("YZ") > 1:
        count += 1
print(count)
