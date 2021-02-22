import random

#Строки
n = 70
#Столбцы
m = 12

a = []

#Средний размер зарплаты
average = 0

#Количество зарплат выше средней
count = 0


for i in range(n):
        a.append([])
        for j in range(m):
            a[i].append(random.randint(20000, 150000))
            average += a[i][j]

#Находим среднее
average /= m * n

for i in range(n):
     for j in range(m):
          if (a[i][j] > average):
               count += 1

print(f"Количество выше средней: {count}")