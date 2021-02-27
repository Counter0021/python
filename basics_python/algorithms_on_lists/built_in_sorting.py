a = [3, 2, 1, 5, 4]
print(a)

a.sort(reverse=True)
print(f"В обратном порядке: {a}")

a.sort()
print(f"В порядке по - умолчанию: {a}")

# Возвращает отсортированный список
a = [3, 2, 1, 5, 4]

print(f"Исходный список: {a}")

print("Вывод отсортированного: ", end="")

for i in sorted(a):
    print(i, "", end="")

print(f"\nИсходный список не изменился: {a}")

b = ["Молоко", "Кефир", "Чай", "Кофе", "Варенье"]

print(b)

b = sorted(b, reverse=True)

print(b)