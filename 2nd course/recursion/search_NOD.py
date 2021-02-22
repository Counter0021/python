# Наибольший общий делитель

# Без рекурсии
#def nod(a, b):
#    while (a != 0 and b != 0):
#        if (a > b):
#            a %= b
#        else:
#            b %= a
#    return a + b
#print(nod(75, 30))

# С рекурсией
def nod(a, b):
    # Базовый случай(конечный)
    if (a == 0 or b == 0):
        return a + b
    if (a > b):
        return nod(a % b, b)
    else:
        return nod(a, b % a)

print(nod(75, 15))