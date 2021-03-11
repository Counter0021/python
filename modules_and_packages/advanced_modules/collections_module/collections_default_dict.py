# Предоставляет отсутствующие значения
from collections import defaultdict

# Можно передавать параметры для предотвращения ошибки
my_dict = defaultdict(lambda: 1)
my_dict[1] = 'a'

print(my_dict[1])
print(my_dict[2])

s = 'Hello'
d = defaultdict(int)
for i in s:
    d[i] += 1
print(sorted(d.items()))
