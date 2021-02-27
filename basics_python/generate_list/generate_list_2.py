a = [input("Введите") for i in range(5)]
b = [int(i) for i in a if (i.isdigit())]
print(a)
print(b)