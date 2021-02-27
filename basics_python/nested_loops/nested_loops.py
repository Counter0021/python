# Вложенный цикл
smile = "\U0001f600"

# while
for number in range(10):
    count = 0
    emoticons = ""
    while (count <= number):
        emoticons += smile
        count += 1
    print(emoticons)

# for
for number in range(10):
    emoticons = ""
    for count in range(number + 1):
        emoticons += smile
    print(emoticons)

# Умножение строк for
for number in range(1, 11):
    print(smile * number)

# Умножение строк while
count = 0
while (count < 11):
    print(smile * count)
    count += 1