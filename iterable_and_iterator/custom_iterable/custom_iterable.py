# Кастомные итераторы
for i in range(1, 10):
    print(i)
print()


# Собственный range()
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    # Сделать класс итератором
    def __iter__(self):
        return self

    # Чтобы сделать объект итератором
    def __next__(self):
        if self.current < self.end:
            number = self.current
            self.current += 1
            return number
        # Чтобы не было бесконечного цикла
        raise StopIteration


first_range = MyRange(1, 10)
for number in first_range:
    print(number)
