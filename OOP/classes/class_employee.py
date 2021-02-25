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

emp1 = Employee("Аркадий", 0)
emp2 = Employee("Дионис", 100000)

print("Сотрудников:", Employee.empCount)
# Вызов методов из класса
Employee.displayEmployee(emp1)
Employee.displayCount(Employee.empCount)