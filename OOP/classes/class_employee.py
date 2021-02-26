# Создание класса рабочие
class Employee:
    # Общий базовый класс для всех сотрудников
    empCount = 0

    # Конструктор
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # Показать сколько рабочих
    def displayCount(self):
        print("Всего сотрудников: %d" % Employee.empCount)

    # Отображать сотрудника
    def displayEmployee(self):
        print(f"Имя: {self.name}, Зарплата: {self.salary}")

    @classmethod
    def classmethod(cls):
        return "метод класса называется", cls

class ToyClass:
    def instancemethod(self):
        return "вызываемый метод экземпляра", self

    @classmethod
    def classmethod(cls):
        return "метод класса называется", cls

    @staticmethod
    def staticmethod():
        return "статический метод называется"

emp1 = Employee("Аркадий", 0)
emp2 = Employee("Дионис", 100000)

print("Сотрудников:", Employee.empCount)
# Вызов методов из класса
Employee.displayEmployee(emp1)
Employee.displayCount(Employee.empCount)

# Пример экземпляра класса
print("welcome".upper())
print(dict.fromkeys("AEIOU"))