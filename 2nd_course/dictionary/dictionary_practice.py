# Изменение словаря
school = {"1a": 20, "2b": 30, "9a": 25, "9c": 5}
print(school)

school["1a"] += 2
school["9a"] -= 5
school["2b"] = 32

school["9b"] = 21
print(school)
del school["9c"]
print(school)

s = 0
for i in school.values():
    s += i

print(s)

# Возврат ключей из значений
def changeKeyValue(obj):
    d = {}
    for i, j in obj:
        d[j] = i
    return d

a = {1: "name", 2: "Ara", 3: "old", 4: "high"}
b = changeKeyValue(a.items())
print(a)
print(b)