# ==========================================================
#                     Наследование
# ==========================================================
# Можно использовать все элементы из класса предка

# Предок
class Car:
    wheels = 4

    def __init__(self, name, color, year, crashed):
        self.name = name
        self.color = color
        self.year = year
        self.crashed = crashed
        print("Car is created")

    # Кто и куда едет
    def drive(self, city):
        print(f"{self.name} is driving to {city}")

    # Изменение цвета
    def change_color(self, new_color):
        self.color = new_color
        print(f"Color is changed to {new_color}")


# Наследник
# Класс грузовиков
class Truck(Car):
    # Изменяем переменную из класса предка
    wheels = 6

    def __init__(self, name, color, year, crashed):
        # Передаём в класс предка
        Car.__init__(self, name, color, year, crashed)
        print("Truck is created")

    # Изменяем метод из класса предка
    def drive(self, city):
        print(f"Truck {self.name} is driving to {city}")

    # Погрузить груз
    def load_cargo(self, weight):
        print(f"The cargo is loaded. Weight is {str(weight)} kg")


man_truck = Truck("Man", "white", 2015, False)

man_truck.drive("Moscow")
print(man_truck.wheels)

print(man_truck.color)
man_truck.change_color("black")
print(man_truck.color)

man_truck.load_cargo(5000)

# ==========================================================
#                       Полиморфизм
# ==========================================================
# Методы с одинаковым названием - разные у объектов разных классов
# Обязательно должен быть уверен, что этот метод есть в классе!!!

# Класс для наследования
# Абстрактный класс. В них нет реализации конкретной реализации методов
class Animal:
    def __init__(self, name):
        self.name = name

    # Животное говорит
    def speak(self):
        # Выбрасываем ошибку
        raise NotImplementedError("Class successor must implement this method")


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    # Собака говорит
    def speak(self):
        print(f"{self.name} is saying woof")


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    # Кошка говорит
    def speak(self):
        print(f"{self.name} is saying meow")


class Mouse(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    # Мышка говорит
    def speak(self):
        print(f"{self.name} is saying pee-pee-pee")


class Fish(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    # Рыба говорит
    def speak(self):
        print(f"{self.name} is saying nothing")


# Создаём объекты
spike = Dog("Spike")
tom = Cat("Tom")
jerry = Mouse("Jerry")
dorry = Fish("Dorry")

# Создаём список из объектов
pet_list = [spike, tom, jerry, dorry]

# При разных объектах вызывается метод именно того класса, к которому принадлежит объект
# Циклом вызываем метод
for pet in pet_list:
    pet.speak()


# Функцией вызываем метод
def pet_voice(pet):
    pet.speak()


# Циклом вызываем функцию
for pet in pet_list:
    pet_voice(pet)
