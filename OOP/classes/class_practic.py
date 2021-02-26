from random import randint


# Создаём класс
class Soldier:
    # Здоровье = аргументу(здоровье)
    def make_health(self, value):
        self.health = value

    # Сеттер - установить имя
    def set_name(self, name):
        self.name = name

    # Сделать удар
    def make_kick(self, enemy):
        # Чтобы вызывать от объекта нужно добавить переменную после self или
        # вообще объявить метод @staticmethod - сделать статическим
        enemy.health -= 20
        print(f"{self.name} бьёт {enemy.name}")
        print("%s = %d" % (enemy.name, enemy.health))

    # Сделать удар 2
    @staticmethod
    def make_kick2(enemy):
        enemy.health -= 20

# Создаём объекты класса
first = Soldier()
second = Soldier()
# Устанавливаем им хп
first.make_health(100)
second.make_health(100)
first.set_name("Первый")
second.set_name("Второй")

# Цикл ударов
while (first.health > 0 and second.health > 0):
    n = randint(1, 2)
    if (n == 1):
        # Удар нанёс первый
        # Вызываем от класса, потому что, если вызвать от объекта, то объект будет наносить удары себе
        first.make_kick(second)

        # Можно вызывать и от объекта
        #first.make_kick2(second)
    else:
        # Удар нанёс второй
        second.make_kick(first)

# Кто выиграл?
if (first.health > second.health):
    print("Первый выиграл")
elif (second.health > first.health):
    print("Второй выиграл")