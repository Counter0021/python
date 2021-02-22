# Вычислить сумму чисел числа
# While
#def summDigit(n):
#    summa = 0
#    while (n > 0):
#        summa += n % 10
#        n //= 10
#    return summa

# Рекурсия
def summDigit(n):
    # Базовый(конечный) случай
    if (n > 0):
        return n % 10 + summDigit(n // 10)
    else:
        return 0

print(summDigit(354))