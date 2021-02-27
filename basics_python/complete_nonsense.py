# Генератор бредовых фраз со списками
import random

# Существительные
nouns = ["Стол",
         "Стул",
         "Человек",
         "Стена",
         "Дерево",
         "Бревно",
         "Клавиатура"]

# прилагательные
adjectives = ["синий",
              "круглый",
              "горький",
              "тихий",
              "ароматный",
              "молодой",
              "большой",
              "тупой"]

# глаголы
Verbs = ["увидел",
         "шёл",
         "будет",
         "сел",
         "растёт",
         "тупит",
         "быть",
         "живёт"]

n = random.randint(0, len(nouns) - 1)
a = random.randint(0, len(adjectives) - 1)
v = random.randint(0, len(Verbs) - 1)

print(f"{nouns[n]} {adjectives[a]} {Verbs[v]}")