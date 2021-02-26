# Создание класса
class Person:
    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    # Деструктор, удаляет объект
    def __del__(self):
        print(f"До Свидания! {self.name} {self.surname}. Вы нам не подошли.")

    # Метод информации о сотрудниках
    def info(self):
        return f"{self.name} {self.surname}, квалификация = {self.qualification}."


# Список персон, создаём объекты
person = [Person("Даниил", "Корж", 2),
          Person("Анна", "Иванова"),
          Person("Аркадий", "Коунтер", 3)]

# Вывод списка
for i in range(len(person)):
    print(person[i].info())

# Сортировка по возрастанию квалификации для нахождения самого слабого.
# Сортировка объект.параметр
person.sort(key=lambda p: p.qualification)
person[0].__del__()
print("Мы очень сожалеем.")
input("Нажмите ENTER для выхода из программы и уволнения всех: ")
# Удаление всех автоматически
