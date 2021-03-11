# Альтернативные типы данных
# counter - класс словаря, предназначенный для подсчёта хашибл объектов
from collections import Counter

number_list = [1, 1, 23, 41, 51, 2, 1, 2, 2, 1, 3, 3, 3]

string = 'afafagaghajkghjfhgakdhfajkfaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffffffffff'

sentence = 'Hello how are you doing? Hello, I\'m fine. How do you do? Hey Hey Hey !'

# Объект Counter
# Ключи - элементы. Значение - количество этих элементов
print(Counter(number_list))

print(Counter(string))

# Сколько слов в предложении
print(Counter(sentence.split(' ')))

# Общее количество элементов
c = Counter(sentence.split(' '))
print(sum(c.values()))

# Очистка счётчика
c.clear()
print(sum(c.values()))

# Список
print(list(c))
# Множество
print(set(c))
# Словарь
print(dict(c))

x = c.items()
print(x)

# Назад
y = Counter(dict(x))
print(y)

# Самые частые элементы
print(c.most_common(2))

# Самые редкие элементы
print(c.most_common()[:-2-1:-1])
