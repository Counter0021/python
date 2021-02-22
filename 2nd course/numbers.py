# Получить число
def getData(a, osnovanie):
    d = 0
    lenght = len(a)

    for i in range(lenght):
        d += a[i] * osnovanie ** i

    return d

# Вывод
def printData(a):
    for i in range(len(a) - 1, -1, -1):
        print(f"{a[i]}", end="")
    print()

#print("Обычное число")
#a = [4, 6, 9, 8, 5, 5]
#printData(a)
#print(getData(a))

#print("\nЗащифрованное число")
#a = [54, 21, 67, 12, 54]
#printData(a)
#print(getData(a))
a = [0, 0, 0, 0, 1]
print(getData(a, 16))