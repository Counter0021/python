# Кортеж, чтобы не запутаться
from collections import namedtuple

# Не помним порядок или запутались
# Похоже на создание классов
Person = namedtuple('Person', 'name surname age gender')
counter = Person(name='Arkady', surname='Counter', age=25, gender='male')
krost = Person(name='Daniil', surname='Krost', age=20, gender='male')
jane = Person(name='Jane', surname='Smith', age=19, gender='female')

print(counter[0])
# Теперь можно так:
print(counter.name)
print(counter.surname)
print(counter.age)

print(krost.name)
print(krost.surname)

# Изменить параметр
print(jane)
jane = jane._replace(surname='Black')
print(jane)