rashod_na_100_km = 0 #Расход топлива на 10км
all_km = 0 # Всего километров
price_litr = 0 # Цена за литр
all_rashod = 0 # Всего литров на всю поездку
all_price = 0 # Общая стоимость бензина
valuta = " " # Единица измерения стоимости
valuta = input("Введите валюту для расчётов: ")
if (valuta == " "):
    valuta = "руб."

while (rashod_na_100_km <= 0):
    rashod_na_100_km = float(input("Введите расход топлива автомобиля на 100 км: "))
    if (rashod_na_100_km <= 0):
        print("Ошибка данных. Значение не может быть 0 или меньше. Повторите ввод.")

while (all_km <= 0):
    all_km = float(input("Введите сколько километров собираетесь проехать: "))
    if (all_km <= 0):
        print("Ошибка данных. Значение не может быть 0 или меньше. Повторите ввод.")

while (price_litr <= 0):
    price_litr = float(input("Сколько стоит литр бензина? "))
    if (price_litr <= 0):
        print("Ошибка данных. Значение не может быть 0 или меньше. Повторите ввод.")

all_rashod = all_km / 100 * rashod_na_100_km
all_price = all_rashod * price_litr

print("Всего затратите топлива:", int(all_rashod * 100) / 100, "л.")
print("Общая цена:", int(all_price * 100) / 100, valuta)
