# Список с количеством просмотров страниц
sites = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(sites) - 1):
    for j in range(len(sites) - 1 - i):
        if (sites[j] < sites[j + 1]):
            sites[j], sites[j + 1] = sites[j + 1], sites[j]

print(sites)