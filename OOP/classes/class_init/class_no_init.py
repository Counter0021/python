# Создание класса
class Person:
    # Сеттер - установить имя и фамилию
    def setName(self, n, s):
        self.name = n
        self.surname = s

p1 = Person()
p1.setName("Ara", "Counter")
print(f"Имя: {p1.name}, Фамилия: {p1.surname}")