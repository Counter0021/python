import sys

# Получаем глубину рекурсии
# с помощью sys.getrecursionlimit()
dep = sys.getrecursionlimit()
print(f"Количество рекурсивных вызовов: {dep}")

# Устанавливаем другое значение
# с помощью sys.setrecursionlimit()
sys.setrecursionlimit(5000)
print(f"Количество рекурсивных вызовов: {sys.getrecursionlimit()}")