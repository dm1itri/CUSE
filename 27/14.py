with open("files/14_a.txt") as f:
    N = int(f.readline())
    sp = list(map(int, f))
min1 = min2 = 0
for i in range(7, N):
    min1 = max(min1, sp[i - 7])
    min2 = max(min2, sp[i] + min1)
print(min2)
