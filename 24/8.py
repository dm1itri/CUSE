with open("8.txt") as f:
    sp = f.readline().replace("W", " ").replace("R", " ").replace("Q", " ").split(" ")

print(len(max(sp, key=len)))

