# Класс автомобиля
class Car:
    # Одинаковые значения для каждого объекта
    wheels = 4

    # Значения для каждого объекта разные
    def __init__(self, name, color, year, crashed):
        self.name = name
        self.color = color
        self.year = year
        self.crashed = crashed

    # Кто и куда едет
    def drive(self, city):
        print(f"{self.name} is driving to {city}")

    # Изменение цвета
    def changed_color(self, new_color):
        self.color = new_color
        print(f"{self.name} painted in {self.color} color")

opel = Car("Opel Tigra", "gray", 1999, True)
opel.drive("Moscow")
opel.changed_color("blue")

mazda = Car("Mazda CX7", "black", 2015, False)
mazda.drive("London")

class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        # Можно вычислять сразу аналог методу get_circumference()
        self.circumference = 2 * self.pi * self.radius

    # Площадь круга
    def get_area(self):
        return self.radius ** 2 * self.pi

    # Длина окружности
    def get_circumference(self):
        return 2 * self.pi * self.radius

circle = Circle()
print(circle.get_area())
print(circle.get_circumference())
print(circle.circumference)

circle_2 = Circle(3)
print(circle_2.get_area())
print(circle_2.get_circumference())
print(circle_2.circumference)