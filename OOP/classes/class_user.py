# Создание класса
class User:
    # Сеттер - установить
    def setName(self, n):
        self.name = n
    # Геттер - получить
    def getName(self):
        try:
            return self.name
        except:
            print("No name")

first = User()
second = User()
first.setName("Ara")
print(first.getName())
print(second.getName())