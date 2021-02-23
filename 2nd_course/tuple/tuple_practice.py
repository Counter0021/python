# Заполнения кортежа + объединение их и подсчёт в них 0
from random import randint

def fill(a, b):
    l = []
    for i in range(10):
        l.append(randint(a, b))
    return tuple(l)

first = fill(0, 5)
second = fill(-5, 0)
third = first + second
count = third.count(0)
print(third)
print(count)