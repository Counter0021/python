class Gamer:
    active_gamers = 0

    # Метод уровня класса - декоратор
    # Активность игроков
    @classmethod
    def get_active_gamers(cls):
        return Gamer.active_gamers

    # Заполнение игрока из строки с данными
    # При помози cls можно создавать объекты, как в __init__()
    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, level, points = data_string.split(" ")
        return cls(nickname, age, level, points)

    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def logOut(self):
        print(f"The player {self.nickname} is out of the game")
        Gamer.active_gamers -= 1

    # Вернуть nickname(ник)
    def get_nickname(self):
        return self.nickname

    # Вернуть age(возраст)
    def get_age(self):
        return self.age

    # Вернуть level(лвл)
    def get_level(self):
        return self.level

    # Вернуть points(очки)
    def get_points(self):
        return self.points

    # Пользователь взрослый?
    def is_adult(self):
        return self.age >= 18

    # Если пользователь взрослый
    def get_adult_level_permission(self):
        if (self.is_adult()):
            print("You can go to adult level")
        else:
            print("You can't go to adult level")

print(Gamer.active_gamers)

gamer_1 = Gamer("_Counter021_", 25, 20, 1022)
gamer_2 = Gamer("krost021", 15, 10, 500)

print(gamer_1.get_age())
gamer_1.get_adult_level_permission()

print(gamer_2.get_age())
gamer_2.get_adult_level_permission()

print(Gamer.active_gamers)

gamer_1.logOut()
print(Gamer.active_gamers)

print(Gamer.get_active_gamers())

counter = Gamer.gamer_from_string("Arkady 25 20 1100")
print(counter.get_nickname())
print(counter.get_age())
print(counter.get_level())

print(Gamer.get_active_gamers())