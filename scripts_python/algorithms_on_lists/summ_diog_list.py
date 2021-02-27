from random import randint

N = 5

# Заполняем и сразу выводим
a = []
for i in range(N):
    a.append([])
    for j in range(N):
        n = randint(1, 9)
        a[i].append(n)
        print("%3d" % n, end="")
    print()

# Находим сумму элементов главной и побочной диагоналей
diagonal1 = 0
diagonal2 = 0
for i in range(N):
    diagonal1 += a[i][i]
    diagonal2 += a[i][N - 1 - i]

print(diagonal1)
print(diagonal2)