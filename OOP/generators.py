# Арифметич. прогрессия типо
# A[] - вычисление значения
A = range(10)

B = (x for x in A if (x % 2 == 0))
# Нельзя print(B)
print(*B)
# * - раскрытие
print(*(x ** 2 for x in A if (x % 2 == 1)))
print(*map(lambda x: x ** 2, A))