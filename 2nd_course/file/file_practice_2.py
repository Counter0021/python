# Чтение из файла
f = open("nums.txt", "r", encoding="utf-8")
ret = []
for i in f.readlines():
    s = i.replace("\n", "")
    s.split("   ")
    ret.append(s)
f.close()
# Сумма
s = 0
for j in range(len(ret)):
    s += int(ret[j])
print(s)