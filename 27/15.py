with open("files/15_b.txt") as f:
    N = int(f.readline())
    sp = list(map(int, f))
min0 = min1 = 10**9
for i in range(5, N):
    min0 = min(min0, sp[i-5])
    min1 = min(min1, sp[i] + min0)
print(min1)