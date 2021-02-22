# Вывод на каждой строке по одной цифре (рекурсия)
def summDigit(n):
    if (n > 0):
        summDigit(n // 10)
        print(n % 10)


print(summDigit(354))