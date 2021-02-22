import random
import  math

count = 0 #количество решенных примеров
right = 0 #Количество правильных ответов
score = 0 #очки
discri = False #Дискриминант

# Основное тело функции проверки на число
def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

# Генерация корней
def randoms():
    global x1, x2, a
    x1 = 0
    x2 = 0
    while not (x1 != 0):
        x1 = random.randint(-10, 10)
        #print(x1)
    while not (x2 != 0):
        x2 = random.randint(-10, 10)
        #print(x2)
    a = 0
    while not (a != 0):
        a = random.randint(-10, 10)

# Генерация корней, цикл на проверку чтобы x1 != -x2
def randomsX1minX2():
    randoms()
    while (x1 == -x2):
        randoms()
    while (a == 1):
        randoms()

# Вычисление коэффициентов для полных квадратных уравнений
def bac():
    global b,c, a
    b = (x1 + x2) * -1 * a
    c = x1 * x2 * a


    #print(x1, x2)

def discr():                               #Дискриминант
    global D, x1, x2, a, b, c
    D = b * b - 4 * a * c
    Dis = math.sqrt(D)
    x1 = (-b + Dis) / (2 * a)
    x2 = (-b - Dis) / (2 * a)
    print(f"""Дикриминант: ",Dis)
x1 = ({-b} + {Dis}) / (2 * {a})
x2 = ({-b} - {Dis}) / (2 * {a})""")
    print(x1,x2)

#Проверка ввода число
def proverka():
    global right, score, discri, count
    x33 = False
    while(x33 != True):
        x3 = input("x1 =")
        x33 = is_digit(x3)

    x44 = False
    while (x44 != True):
        x4 = input("x2 =")
        x44 = is_digit(x4)
    x3 = float(x3)
    x4 = float(x4)

    # Проверка результатов
    if ((x3 == x1 and x4 == x2) or (x3 == x2 and x4 == x1)):
        print("Победа! Поздравляем!")
        right += 1
        score += 10
    else:
        print(f"Вы проиграли правильный ответ: {x1} и {x2} ")
        discri = True
        score -= 20
    count += 1

#Вывод с дискриминантом
def proverkaDiscriminanta():
    if (discri == True):
        discr()

# Подсказки
def podscazka1():
    print("""Это подсказка.
1 - ax^2 + bx = 0
x(ax+b) = 0
x = 0 v ax+b = 0
        x = -b/a
Пример:
    2 x^2  -16 x = 0
    x(2x - 16) = 0
    x = 0 v 2x - 16 = 0
            2x = 16
            x = 8
Ответ: x1 = 0, x2 = 8""")

def podscazka2():
    print("""2 - ax^2 + c = 0
x^2 = -c / a
x = √-c/a
Пример:
    -10x^2 + 90 = 0
    x^2 = 90/10
    x^2 = 9
    x = √9
    x = ±3
Ответ: x1 = 3, x2 = -3""")

def podscazka3():
    print("""3 - ax^2 = 0
Пример:
    10x^2 = 0
    x = 0
Ответ: x = 0""")

def podscazka4():
    print("""4 - x^2 + bx + c = 0
{x1 + x2 = -b
{x1 * x2 = c
Пример:
    x^2 + 3 x -4 = 0        
    {x1 + x2 = -3   {x1 = -4
    {x1 * x2 = -4   {x2 = 1
Ответ: x1 = -4, x2 = 1""")

def podscazka5():
    print("""5 - ax^2 + bx + c = 0
D = b^2 - 4ac
x = (-b ± √D) / (2a)
x1 = (-b - √D) / (2a)
x2 = (-b + √D) / (2a)
Пример:
    6x^2 -54x + 48 = 0
    D = 2916 - 1152 = 1764
    √D = 42
    x1 = (54 - 42) / 12 = 1
    x2 = (54 + 42) / 12 = 8
Ответ: x1 = 1, x2 = 8""")

# *************************************************************
#                   Функции уранений
# *************************************************************

# 1 - ax^2 + bx = 0
def form1():
    global right, score, x1

    randomsX1minX2()

    x1 = 0

    b = x2 * a * -1

    print(x1, x2)

    if (b < 0):
        print(f"{a} x^2  {b} x = 0")
    else:
        print(f"{a} x^2 + {b} x = 0")

    proverka()

# 2 - ax^2 + c = 0
def form2():
    global right, score, x2

    randomsX1minX2()
    x = x1
    x2 = -x1
    xv2 = x ** 2
    c = (xv2 * -1 * a)

    print(x,x2)

    if (c != 0):
        if (c > 0):
            print(f"{a}x^2 + {c} = 0")
        else:
            print(f"{a}x^2 {c} = 0")

    proverka()

# 3 - ax^2 = 0
def form3():
    global right, score, x1, x2

    randoms()
    x1 = 0
    x2 = 0
    print(f"{a} x^2 = 0")

    proverka()

# 4 - x^2 + bx + c = 0
def form4():
    global right, score, a

    randomsX1minX2()
    a = 1
    bac()

    if (b <= 0 and c <= 0):
        print(f"x^2 {b} x {c} = 0")
    elif (b <= 0 and c >= 0):
        print(f"x^2 {b} x + {c} = 0")
    elif (b >= 0 and c >= 0):
        print(f"x^2 + {b} x + {c} = 0")
    else:
        print(f"x^2 + {b} x {c} = 0")

    proverka()

# 5 - ax^2 + bx + c = 0
def form5():
    global right, score

    randomsX1minX2()
    bac()

    if (b <= 0 and c <= 0):
        print(f"{a}x^2 {b}x {c} = 0")
    elif (b <= 0 and c >= 0):
        print(f"{a}x^2 {b}x + {c} = 0")
    elif (b >= 0 and c >= 0):
        print(f"{a}x^2 + {b}x + {c} = 0")
    else:
        print(f"{a}x^2 + {b}x {c} = 0")

    proverka()

# Подсказка выбор
def form6():
    def centr():
        # Цикл для выбора подсказки
        while True:
            print("Для выхода из подсказки введите a, для выхода из программы введите s")
            c = input("ВВедите подсказку: ")
            execute(c, podscazka)

    podscazka = {
        '1': podscazka1,
        '2': podscazka2,
        '3': podscazka3,
        '4': podscazka4,
        '5': podscazka5,
        'a': main,
        's': exit
    }
    centr()

def form7():                                    #Показать статистику
    print(f"""Ваше количество очков: {score}
Количество правильных решений: {right}
Количество примеров: {count}""")


# Приветствие
print("""Здравствуйте!
Я сделал эту программу для того, чтобы вы научились решать любые квадратные уравнения.
Для этого просто выберите режим (1-5)
1 - ax^2 + bx = 0 (неполное квадратное уравнение c = 0)
2 - ax^2 + c = 0 (неполное квадратное уравнение b = 0)
3 - ax^2 = 0 (неполное квадратное уравнение b = 0 и c = 0)
4 - x^2 + bx + c = 0 (полное приведенное квадратное уравнение)
5 - ax^2 + bx + c = 0 (полное неприведённое квадратное уравнение)
6 - Подсказки, если не знаешь как решать(они с примерами)
7 - Статистика игры""")

# Главный метод
def main():
    while True:
        global g
        # Запрашиваем переменную для ввода режима
        g = input("Введите режим, Для выхода введите s: ")
        execute (g, dictOfCommands)

dictOfCommands = {
        '1': form1,
        '2': form2,
        '3': form3,
        '4': form4,
        '5': form5,
        '6': form6,
        '7': form7,
        's': exit
}

# Проверка: "есть-ли выбранная команда в словаре list?"
def execute(command, list):
    try:
        list[command]()
    except KeyError:
        print('Неизвестная команда, пробуй еще раз')

# Запуск основного тела программы
main()