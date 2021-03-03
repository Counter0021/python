# # Ввод
# x = input("Input something ")
#
# # Вывод
# print(f"Output something {x}")

# ============================================
#                   Файл
# ============================================
lorem_ipsum_text = open("file/sample.txt", "r", encoding="utf-8")
for line in lorem_ipsum_text:
    print(line, end="")

lorem_ipsum_text.close()

lorem_ipsum_text = open("file/sample.txt", "r", encoding="utf-8")
for line in lorem_ipsum_text:
    if "mary" in line.lower():
        print(line, end="")

lorem_ipsum_text.close()

# ============================================
#            Оператор with
#        Автоматом закрывает файл
# ============================================
with open("file/sample.txt", "r", encoding="utf-8") as lorem_ipsum_text:
    for line in lorem_ipsum_text:
        if "mary" in line.lower():
            print(line, end="")

# ============================================
#          readline() - одна строка
# ============================================
with open("file/sample.txt", "r", encoding="utf-8") as lorem_ipsum_text:
    line = lorem_ipsum_text.readline()
    while line:
        print(line, end="")
        line = lorem_ipsum_text.readline()

# ============================================
#            readlines() - все строки
#           Сохраняет строки в список
# ============================================
with open("file/sample.txt", "r", encoding="utf-8") as lorem_ipsum_text:
    lines = lorem_ipsum_text.readlines()

for line in lines[::-1]:
    print(line, end="")

# ============================================
#       read() - весь текст в 1 пременной
# ============================================
with open("file/sample.txt", "r", encoding="utf-8") as lorem_ipsum_text:
    text = lorem_ipsum_text.read()
print(text)