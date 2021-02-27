# Заполнение словаря
number_dict = {"first": 1, "second": 2, "third": 3}
new_dict = {key: value ** 3 for key, value in number_dict.items()}
print(new_dict)

number_list = [6, 45, -15, -56, 65, 0]
number_dict_1 = {number: number ** 2 for number in number_list}
print(number_dict_1)

number_dict_1 = {number: "+" if (number > 0)
else "-" if (number < 0) else "zero" for number in number_list}
print(number_dict_1)

# ============================================
print()
# ============================================

# Заполнение множеств
number_list = [6, 45, -15, -56, 65, 0]
number_set = {number ** 2 for number in number_list}
print(number_set)

number_set_2 = {number ** 2 for number in range(3, 11)}
print(number_set_2)

letter_set = {letter.upper() for letter in "hello"}
print(letter_set)