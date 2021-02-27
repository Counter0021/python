# Функция для проверки
def commands(comm):
    global cleanCommand
    cleanCommand = ""
    # Проверяем, устанавливая счётчиком цикла каждый символ в строке команд последовательно
    for i in comm:
        # Если код символа есть в списке кодов
        if (ord(i) in codeList):
            # Добавляем символ к "очищенной строке"
            cleanCommand += i
    return cleanCommand

# Задаём список и помещаем в него коды правильных символов-команд
codeList = []
for i in "WASDE0123":
    codeList.append(ord(i))

# Запрашиваем команды (как бы пришли они по радио связи)
comm1 = input("Введите команды Копатыча: ")
comm2 = input("Введите команды Копатыча: ")
comm3 = input("Введите команды Копатыча: ")

# Переменная для новой, чистой строки
cleanCommand = ""

# Очищенная строка 3 раза
commands(comm1)
cleanCommand1 = cleanCommand

commands(comm2)
cleanCommand2 = cleanCommand

commands(comm3)
cleanCommand3 = cleanCommand

# Если команды совпадают
if (cleanCommand1 == cleanCommand2 == cleanCommand3):
    # Выводим на экран (или отправляем процессору Копатыча)
    print(f"Очищенная строка: {cleanCommand}")
else:
    print("Комманды не совпадают")