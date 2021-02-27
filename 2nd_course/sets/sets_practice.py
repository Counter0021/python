print("Чтобы остановить введите 'stop'")

# Множество
tags = set()

phrase = ""
while (phrase != "stop"):
    phrase = input("Введите тег: ")
    if (phrase in tags):
        print("Этот тег уже есть")
        continue
    if (phrase != "stop"):
        tags.add(phrase)

print(tags)
