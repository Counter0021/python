# Список для замены
words = ["один", "два", "три", "четыре", "пять"]

# Чтение из файла и запись в список
f = open("words.txt", "r", encoding="utf-8")
word = []
for i in f:
    word.append(i[:-1])
f.close()

# Запись в новый файл изменённых слов
f = open("wordsRu.txt", "w", encoding="utf-8")
for i in range(len(word)):
    word[i] = words[i]
    f.writelines(word[i] + "\n")
f.close()