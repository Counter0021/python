import random

n = 5
m = 9

a = []

for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(random.randint(10, 99))

mx = a[0][0]
mn = a[0][0]

for i in range(n):
    for j in range(m):
        # Последовательно сравниваем каждый элемент
        # с mx и mn: так мы найдем максимальное
        # Если меньше mn, то помещаем в mn - так найдём минимальное
        if (a[i][j] > mx):
            mx = a[i][j]
        if (a[i][j] < mn):
            mn = a[i][j]

print(f"Максимальное: {mx}")
print(f"Минимальное: {mn}")
