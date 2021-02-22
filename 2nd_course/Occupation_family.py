import random

name = ["Анжелика",
        "Лилиана",
        "Леонид",
        "Сергей",
        "Аркадий"]

#Не играет в комп
no_play_pc = random.randint(0, len(name) - 1)
#Моет полы
wash_floors = random.randint(0, len(name) - 1)
#Угощает всех пиццей
Treats_with_pizza = random.randint(0, len(name) - 1)
#Молчит весь день
Is_silent_all_day = random.randint(0, len(name) - 1)

print("Не играет в комп:", name[no_play_pc])
print("Моет полы:", name[wash_floors])
print("Угощает всех пиццей:", name[Treats_with_pizza])
print("Молчит весь день:", name[Is_silent_all_day])