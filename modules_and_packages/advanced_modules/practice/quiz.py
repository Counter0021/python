# Вопросы

import time
from random import randint


# Пользователь завершил игру
def win():
    global end
    # Время в конце
    end = time.perf_counter()
    print(f'Congratulations! Your total score is: {count}, total time is {round(end - start)} seconds!')


# Символ введён правильный?
def extra_characters():
    answer = input('Please enter T if it is true and F if it is false: ').upper()
    if answer in valid_characters:
        answer_list.append(answer)
    else:
        extra_characters()


# Метод с выводом рандомных вопросов
def main():
    global count
    # Рандом числа
    rand = randint(0, len(questions_answers) - 1)

    print('True or false: ', questions_answers[rand][0])
    # Проверка символа
    extra_characters()
    # Если ответ верный
    if answer_list[-1] == questions_answers[rand][1]:
        print('Excellent!')
        count += 1
    else:
        print('Not correct:( Maybe you will be lucky next time!')
    # Удаляем элемент из списка с вопросами
    del questions_answers[rand]

    # Если длина списка равна 0
    if len(questions_answers) == 0:
        win()


# Список для вопросов
questions_answers = []
# Заполнение вопросами списка
questions_answers.append(['The epoch is the point where the time starts, \
and is platform independent.', 'F'])
questions_answers.append(['For Unix, the epoch is January 1, 1970, 00:00:00 (UTC).'
                             , 'T'])
questions_answers.append(['The term seconds since the epoch refers to the \
total number of elapsed seconds since the epoch', 'T'])
questions_answers.append(['Function strptime() can parse \
4-digit years when given %y format code.', 'F'])
questions_answers.append(['UTC is Coordinated Universal Time.', 'T'])
questions_answers.append(['DST is Daylight Saving Time, an adjustment \
of the timezone by (usually) two hours during part of the year.', 'F'])
questions_answers.append(['The time value as returned by gmtime(), \
localtime(), and strptime(), and accepted by asctime(), mktime() and \
strftime(), is a sequence of 9 integers.', 'T'])

# Список с ответами пользователя
answer_list = []

# Разрешённые символы
valid_characters = ['F', 'T']

# Запуск кода
if __name__ == '__main__':
    input('Input enter to start ')
    # Время при старте
    start = time.perf_counter()
    # Время в конце
    end = None
    # Счётчик правильных ответов
    count = 0

    # Цикл вызова главного метода
    for i in range(len(questions_answers)):
        main()
