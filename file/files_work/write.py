# Запись
colors_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
with open("file/rainbow_colors.txt", "w", encoding="utf-8") as rainbow_colors:
    for color in colors_list:
        print(color, file=rainbow_colors)

# Добавить
with open("file/rainbow_colors.txt", "a", encoding="utf-8") as rainbow_colors:
    print("dark green", file=rainbow_colors)
    print("dark blue", file=rainbow_colors)

# Чтение
colors_list = []
with open("file/rainbow_colors.txt", "r", encoding="utf-8") as rainbow_colors:
    for color in rainbow_colors:
        colors_list.append(color.strip('\n'))
print(colors_list)