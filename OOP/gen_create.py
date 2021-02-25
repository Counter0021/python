# Создание генераторов

def arithm_progression(start, stop, step):
    x = start
    while (x < stop):
        print(f"now working on x = {x}")
        yield x
        x += step

A = arithm_progression(1, 10, 2)

for x in A:
    print(x)