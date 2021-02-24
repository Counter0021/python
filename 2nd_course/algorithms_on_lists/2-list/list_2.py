# Вывод списка по строчно с изменением отрицательного числа на положительное
from random import randint

n = 4
m = 4
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        r = randint(-9, 9)
        a[i].append(r)
print(a, end="\n\n")

for o in range(n):
    for p in range(m):
        if (a[o][p] > 0):
            print("%3d" % a[o][p], end="")
        else:
            print("  -", end="")
    print()