# Заполнение списка
greeting = "hello!"
letter_list = [letter for letter in greeting]
print(letter_list)
number_list = [number for number in "0123456789"]
print(number_list)
number_list_1 = [num for num in range(10)]
print(number_list_1)
number_list_2 = [num ** 2 for num in range(10)]
print(number_list_2)
number_list_3 = [- ((num - 3) / 2) ** 2 for num in range(10)]
print(number_list_3)

# =======================================================
print()
# =======================================================
numbers_list = [6, 43, 22, -51, 5, 25, -50]
new_list = [number ** 2 for number in numbers_list if (number > 0)]
print(new_list)

new_list_1 = ["+" if (number > 0) else "-" for number in numbers_list]
print(new_list_1)