# Функция zip
A = (1, 2, 3, 4, 5)
# Генератор
B = tuple(x * 10 for x in A)
print(A)
print(B)

C = zip(A, B)
# Делаем кортежи
for t in C:
    print(t)

# Сразу распаковка
for a, b in zip(A, B):
    print(a, b, a + b)

# Пронумеровать, возвращаются кортежи, прицепляет к нему номерки
for i, char in enumerate("HELLO"):
    print(i, char)