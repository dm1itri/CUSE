"""https://education.yandex.ru/ege/task/3ec50c37-de04-4705-9674-5dfd1284dd9f"""

with open("trucks_cargo.txt") as f:
    n, weight_max = map(int, f.readline().split())
    cargos = sorted(map(int, f.readlines()))
weight = 0
new_sp_310 = []
for cargo in cargos[:]:
    if 310 <= cargo <= 320:
        weight += cargo
        cargos.remove(cargo)
        new_sp_310.append(cargo)

new_sp = []
for cargo in cargos[:]:
    if weight + cargo <= weight_max:
        weight += cargo
        new_sp.append(cargo)
        cargos.remove(cargo)

t = True
for i in range(len(new_sp) - 1, -1, -1):
    if t:
        t = False
        for j in range(len(cargos) - 1, -1, -1):
            if weight - new_sp[i] + cargos[j] > weight_max:
                cargos.pop(j)
            elif cargos[j] > new_sp[i]:
                weight += -new_sp[i] + cargos[j]
                new_sp[i] = cargos.pop(j)
                t = True
                break


print(len(new_sp_310 + new_sp))
print(weight)
