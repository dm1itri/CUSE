with open("files/7_b.txt") as f:
    n = int(f.readline())
    sp = list(map(int, f))
arr = [[10**9, 10**9]] + [10**9] * 92
for i in sp:
    if i % 93 == 0:
        if i < arr[0][0]:
            arr[0][0] = i
        elif i < arr[0][1]:
            arr[0][1] = i
    else:
        arr[i % 93] = min(arr[i % 93], i)
min_s = arr[0][0] + arr[0][1]
for i in range(1, 47):
    min_s = min(min_s, arr[i] + arr[93 - i])
print(min_s)

