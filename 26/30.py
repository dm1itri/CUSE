"""Предприятие производит закупку изделий A и B, на которую выделена определённая сумма денег. У
поставщика есть в наличии различные модификации этих изделий по различной цене. При покупке
необходимо руководствоваться следующими правилами: 1. Нужно купить как можно больше изделий,
независимо от их типа и модификации. 2. Если можно разными способами купить максимальное
количество изделий, нужно выбрать тот способ, при котором будет куплено как можно больше изделий
B. 3. Если можно разными способами купить максимальное количество изделий с одинаковым
количеством изделий B, нужно выбрать тот способ, при котором вся покупка будет дешевле.
Определите, сколько всего будет куплено изделий B и какая сумма останется неиспользованной.
Входные данные Первая строка входного файла содержит два целых числа: N – общее количество
изделий у поставщика и M – сумма выделенных на закупку денег (в рублях). Каждая из следующих N
строк содержит целое число (цена изделия в рублях) и символ (латинская буква A или B),
определяющий тип изделия. Все данные в строках входного файла отделены одним пробелом. В ответе
запишите два целых числа: сначала количество закупленных изделий типа B, затем оставшуюся
неиспользованной сумму денег. Пример входного файла 6 130 30 A 50 A 60 B 20 B 70 B 10 A В данном
случае можно купить не более 4 изделий, из них не более 2 изделий B. Минимальная цена такой
покупки 120 рублей (покупаем изделия 30A, 60B, 20B, 10A). Останется 10 рублей. В ответе надо
записать числа 2 и 10."""

with open("30.txt") as f:
    N, M = map(int, f.readline().split())
    sp = sorted((int(x.split()[0]), x.split()[1] == "B") for x in f.readlines())
count_B = 0
prices_A = []
for price, name in sp:
    if price <= M and name:
        M -= price
        count_B += 1
    elif price <= M:
        M -= price
        prices_A.append(price)
    elif price - prices_A[-1] <= M and name:
        M -= price - prices_A.pop(-1)
        count_B += 1

print(count_B, M)
