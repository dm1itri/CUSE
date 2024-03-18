with open("25.txt") as f:
    sp = [i for i in f.readline().split("A") if i.count("B") >= 3]
print(len(max(sp, key=len)))
