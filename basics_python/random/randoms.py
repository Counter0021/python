from random import random, randint, randrange, shuffle

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

# Перемешать элементы рандомно shuffle()
my_list = [1, 3, 56, 4]
print(my_list)
shuffle(my_list)
print(my_list)