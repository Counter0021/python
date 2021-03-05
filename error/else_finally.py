while True:
    try:
        number = int(input('Enter some number: '))
        print(number / 2)
    except:
        print('You have to enter a number!')
    # Срабатывает, когда нет ошибки
    else:
        print('Good job! This is a number!')
        break
    # Выполняется всегда
    finally:
        print('Finally block')


def divide(x, y):
    try:
        print(x / y)
    except ZeroDivisionError as e:
        print("You can't divide by zero")
        print(e)
    # Для вывода названия ошибки: as valuable
    except TypeError as e:
        print('x and y must be number')
        print(e)
    else:
        print('x was divided by y')
    finally:
        print('Finally block')


# divide(4, 2)
divide(4, 0)
divide(4, '5')