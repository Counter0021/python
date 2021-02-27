count = 0
for i in range(1, 10):
    for j in range(10):
        for o in range(10):
            if ((i + j + o) % 25 == 0):
                count += 1
                print(f"{i}{j}{o}")

print(f"Всего: {count} чисел")