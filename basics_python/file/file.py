# ===================================== Чтение =====================================
# Чтение файла .read()
f = open("data.txt", "r", encoding="utf-8")
print(f.read())
f.close()

# Чтение построчно .readline()
f = open("data.txt", "r", encoding="utf-8")
print(f.readline())
f.close()

# Чтение всех строк и создание списка
f = open("data.txt", "r", encoding="utf-8")
print(f.readlines())
f.close()

# Без методов чтения
for i in open("data.txt"):
    print(i)
f.close()

# Без "\n"
nums = []
for i in open("data.txt"):
    nums.append(i[:-1])
print(nums)
f.close()

# ===================================== Запись =====================================
# Запись в файл .write()
f = open("newdata.txt", "w", encoding="utf-8")
f.write("one")
f.close()

# Запись в файл структуры данных .writelines
l = ["two", "tree"]
f = open("newdata.txt", "w", encoding="utf-8")
f.writelines(l)
f.close()

# Чтобы узнать закрыт файл .closed
print(f.closed)