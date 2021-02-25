# Создание класса прямоугольник
class Rectangle:
    # Стандарт цвет
    default_color = "green"

    # Конструктор
    def __init__(self, width, height):
        # Ширина = ширине(передоваемой в функцию)
        self.width = width
        # Высота = высоте(передоваемой в функцию)
        self.height = height


# Отправляем параметры в класс
rect = Rectangle(1, 2)

# Изменяем класс
print("Стандарт(зелёный)", Rectangle.default_color)
Rectangle.default_color = "red"
print("Красный", Rectangle.default_color)

# Создаём новые переменные с параметрами класса
r1 = Rectangle(2, 3)
r2 = Rectangle(3, 10)

# Изменяем их
r1.default_color = "blue"
print("Синий", r1.default_color)
print("Без изменений", r2.default_color)