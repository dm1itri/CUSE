with open("34.txt") as f:
    s = "A" + f.readline() + "A"
sp = [(i, s[i]) for i in range(len(s)) if s[i] in "AB"]
max_len = 0
for i in range(3, len(sp) - 1):
    sp_curr = [sp[i - 3][1], sp[i - 2][1], sp[i - 1][1], sp[i][1]]
    if sp_curr.count("A") == 2:
        max_len = max(max_len, sp[i + 1][0] - sp[i - 4][0] - 1)
    elif (sp_curr.count("A") == 3 or sp_curr.count("B") == 3) and sp_curr[0] == sp_curr:
        max_len = max(max_len, sp[i + 1][0] - sp[i - 3][0] - 1)
print(max_len)
