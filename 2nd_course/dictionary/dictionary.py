# Словарь
a = {}
a["cat"] = "кошка"
a["dog"] = "собака"
print(a)
a["dog"] = "пёс"
print(a)
del a["cat"]
print(a)

b = {"name": "Ara", 1: [10, 15, 20], 2: 32, ("ab", 100): "no"}
print(b[("ab", 100)])
print(b[1])

nums = {1: "one", 2: "two", 3: "three"}
# Ключи
for i in nums:
    print(i)

# Значения
for i in nums:
    print(nums[i])

# Структура из кортежей .items()
n = nums.items()
print(n)

# Распаковка кортежей, извлекая ключ и значение
for key, value in nums.items():
    print(key, "is", value)

# Распаковка значений .values()
nums_value = []
for v in nums.values():
    nums_value.append(v)
print(nums_value)

# Распаковка ключей .keys()
nums_key = []
for k in nums.keys():
    nums_key.append(k)
print(nums_key)

# Удаление всего, кроме самого словаря .clear()
dict1 = {1: 2, 4: "f", "k": 3}
print(dict1)
dict1.clear()
print(dict1)

# Копирование словаря .copy()
nums2 = nums.copy()
nums2[1] = "Arkadiy"
print(nums)
print(nums2)

# Создание словаря из списка с ключами .fromkeys()
c = [1, 3, 4]
d = dict.fromkeys(c)
print(c)
print(d)
e = dict.fromkeys(c, 20)
print(e)

# Получить элемент по ключу .get()
key1 = nums.get(1) # = nums[1]
print(key1)

# Удаление элемента по ключу и возвращение значения удалённой пары .pop()
print(nums.pop(2))
print(nums)

# Удаление и возвращение произвольного элемента .popitem()
print(nums.popitem())
print(nums)

# Добавление элемента в словарь .setdefault(), не перезаписывает значение, если элемент есть
nums.setdefault(4, "four")  # = nums[4] = "four"
print(nums)

# Добавление словаря в другой словарь .update()
nums.update({6: "six", 7: "seven"})
print(nums)