import random
        # 1 - ax^2 + bx + c = 0
        # 2 - ax^2 + bx = 0
        # 3 - ax^2 + c = 0
        # 4 - ax^2 = 0

def form1():
    x1 = random.randint(1, 10)
    x2 = random.randint(1, 10)
    a = random.randint(1, 10)

    b = (x1 + x2) * -1
    c = x1 * x2
    print(f"x^2 + {b} x + {c} = 0")
    print("Корни уравнения X1=",x1,"X2=",x2)

def form2():
    x2 = random.randint(1, 100)
    a = random.randint(1, 100)
    x1 = 0
    b = x2 * a * -1
    print(f"{a} x^2  {b} x = 0")

def form3():
    aa = random.randint(-10,10)
    x = random.randint(-10,10)
    x22 = x ** 2
    c = x22 * -1
    if (x22 > 0):
        print(f"{aa}x^2  {c * aa} = 0")
    else:
        print(f"{aa}x^2+ {c * aa} = 0")

def form4():
        a = random.randint(1, 10)
        x = 0
        print(f"{a} x^2 = 0")

print("Выбери режим (1-4)")
print("1 - ax^2 + bx + c = 0")
print("2 - ax^2 + bx = 0")
print("3 - ax^2 + c = 0")
print("4 - ax^2 = 0")

def main():
    while True:
        g = input("ВВеди режим_")
        execute (g)

dictOfCommands = {
        '1': form1,
        '2': form2,
        '3': form3,
        '4': form4,
        'l': exit
}

def execute(command):
    try:
        dictOfCommands[command]()
    except KeyError:
        print('Неизвестная команда, пробуй еще раз')

main()