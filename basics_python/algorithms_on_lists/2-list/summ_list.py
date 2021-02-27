# Сумма столба списка
from random import randint

n = 3
m = 4
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(randint(1, 9))

for i in range(n):
    for j in range(m):
        print("%3d" % a[i][j], end="")
    print()
print()

for j in range(m):
    s = 0
    for i in range(n):
        s += a[i][j]
    print("%3d" % s, end="")
print()