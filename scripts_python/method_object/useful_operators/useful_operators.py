# Печать индексов последовательности
# С циклом
letter_index = 0
my_string = "afagag"
for letter in my_string:
    print(letter + " индекс " + str(letter_index))
    letter_index += 1

# ========================================================
print()
# ========================================================

# С функцией .enumerate()
for index, item in enumerate(my_string):
    print(item + " индекс " + str(index))

# ========================================================
print()
# ========================================================
# Находится ли символ в строке
print("a" in "Arkady")

# Находится ли символ в списке
letter_list = ["a", "b", "c"]
print("a" in letter_list)

# ========================================================
print()
# ========================================================
# Находится ли символ в словаре
dict_1 = {1: "a", 2: "b", 3: "c"}
print(1 in dict_1.keys())
print("a" in dict_1.values())

# ========================================================
print()
# ========================================================
# min и max
print(min(1, 2, 5))
print(max(2, 8, 1))

my_list = [1, 2, 65]
print(min(my_list))
print("Символ максимальны: ", max(my_list))

print(max("hello"))
for letter in "hello":
    print(ord(letter))
