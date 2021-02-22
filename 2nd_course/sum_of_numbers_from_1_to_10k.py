summ = 0
n = 10000

for i in range(1, n + 1):
    summ += i
print(summ)

#Второй вариант
n = 10000
summ = n * (n + 1) // 2
print(summ)