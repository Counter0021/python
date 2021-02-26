# Создание класса
class Person:
    # Конструктор
    # Устанавливаем имя и фамилию
    def __init__(self, n, s):
        self.name = n
        self.surname = s

p1 = Person("Arkady", "Counter")
print(f"{p1.name} {p1.surname}")