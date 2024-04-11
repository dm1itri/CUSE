with open("files/1_b.txt") as f:
    n = int(f.readline())
    sp = list(map(int, f))
arr = [0] * 3
for i in sp:
    if i % 6 == 0:
        arr[2] += 1
    elif i % 3 == 0:
        arr[1] += 1
    elif i % 2 == 0:
        arr[0] += 1
print(arr[2]*(n - arr[2]) + arr[2] * (arr[2] - 1) // 2 + arr[1] * arr[0])