# Специальные методы __метод__
# Можно переопределять. Методы смотреть в документации:
# https://docs.python.org/3/reference/datamodel.html#special-method-names

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    # Переопределяем метод __str__
    # Вывод будет имя и фамилия, а не адрес объекта при использовании print()
    def __str__(self):
        return f"{self.name} {self.surname}"

    # Переопределяем метод __len__
    # Длины
    def __len__(self):
        return self.age

    # Переопределяем метод __del__
    # Удаление объекта. Деструктор - вызывается всегда для удаления мусора
    def __del__(self):
        print(f"Object {self.name} is deleted")

    # Переопределяем метод __add__
    # Сложение
    def __add__(self, other):
        return self.age + other.age


arkady = Person("Arkady", "Counter", 25)
daniil = Person("Daniil", "Korj", 18)
print(arkady)
print(len(arkady))
print(arkady + daniil)
del arkady
