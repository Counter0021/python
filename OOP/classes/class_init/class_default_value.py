# Создание класса
class Rectangle:
    # Конструктор класса
    # Ширина и высота прямоугольника
    # Выставляем значения по умолчанию для того,
    # чтобы допустить создание класса без параметров
    def __init__(self, w=0.5, h=1):
        self.width = w
        self.height = h

    # Метод вычисление площади
    def square(self):
        return self.width * self.height

# Создаём объекты
rec1 = Rectangle(5, 2)
rec2 = Rectangle()
rec3 = Rectangle(3)
rec4 = Rectangle(h=4)
print(rec1.square())
print(rec2.square())
print(rec3.square())
print(rec4.square())