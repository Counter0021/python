# Форматирование строк
name = "Arkady"
age = 25
# Указываем в {} параметр по счёту
name_and_age = "My name is {0} I\'m {1} years old.".format(name, age)
print(name_and_age)

week = "В неделе 7 дней: {5}, {0}, {2}, {1}, {3}, {4}, {6}.".format("Пон", "Среда", "Вт", "Чт", "Пят", "Вск", "Суб")
print(week)
week_2 = "В неделе 7 дней: {sun}, {m}, {t}, {w}, {tu}, {f}, {sut}.".format(m="Пон", w="Среда", t="Вт", tu="Чт", f="Пят",
                                                                      sun="Вск", sut="Суб")
print(week_2)
float_res = 1000 / 7
print(float_res)
# f - значит тип данных float
print("Результат = {0:4.3f}".format(float_res))