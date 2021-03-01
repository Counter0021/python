# Множественное наследование
# Способность - умеющий плавать
class Swimmable:
    def __init__(self, name):
        self.name = name

    # Приветсвие
    def greeting(self):
        print(f"Hello! My name is {self.name} and I can swim")

    # Я плыву
    def swim(self):
        print("I'm swimming")


# Ходить
class Walkable:
    def __init__(self, name):
        self.name = name

    # Приветсвие
    def greeting(self):
        print(f"Hello! My name is {self.name} and I can walk")

    # Я гуляю
    def walk(self):
        print("I'm walking")


# Летать
class Flyable:
    def __init__(self, name):
        self.name = name

    # Приветсвие
    def greeting(self):
        print(f"Hello! My name is {self.name} and I can fly")

    # Я летаю
    def fly(self):
        print("I'm flying")


# Персонаж игры
class GameCharacter(Swimmable, Walkable, Flyable):
    def __init__(self, name):
        self.name = name
        Swimmable.__init__(self, name)
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)

    # Приветсвие
    # def greeting(self):
    #     print(f"Hello! My name is {self.name}")


james = GameCharacter("James")
james.greeting()
james.walk()
james.swim()
james.fly()

# Проверка - является ли объект определённого класса. Метод isinstance()
print(isinstance(james, Swimmable))