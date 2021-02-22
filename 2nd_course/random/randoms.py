from random import random, randint, randrange

# Рандом вещественного числа .random()
# Чтобы число было > 0, нужно умножить его на любое целое
a = random() * 10
print(a)
# Округлить результат
print(round(a, 2))

# Рандом числа в диапазоне с учётом конечного числа .randint()
print(randint(0, 10))

# Рандом числа в диапазоне без учёта конечного числа .randrange()
# 3 аргумент - шаг(3, 6, 9)
print(randrange(0, 10, 3))