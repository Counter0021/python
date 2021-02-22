# Функция для очистки команд
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

# Создаём список команд
comm = []
# Создаём список чистых команд
cleanCommands = []

# Запрашиваем команды (как бы пришли они по радио связи)
# Вносим их в список
for i in range(3):
    command = input("Введите команды Копатыча: ")
    comm.append(command)

# Переменная для новой, чистой строки
cleanCommand = ""

# Чистим команды и Вносим чистые команды в новый список
for i in range(len(comm)):
    commands(comm[i])
    x = cleanCommand
    cleanCommands.append(x)

# Проверка совпадения команд
if (cleanCommands[0] == cleanCommands[1] == cleanCommands[2]):
    # Выводим на экран (или отправляем процессору Копатыча)
    print(f"Очищенная строка: {cleanCommand}")
else:
    print("Комманды не совпадают")