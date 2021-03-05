import time

# Сравнение генераторов и списков

# Список
# Сразу создаётся список и потом складывается
print(sum([i for i in range(10)]))

# Генератор
# Создаётся 1 элемент в 1 момент времени
print(sum(i for i in range(10)))

start_time_list = time.time()
print(sum([i for i in range(100000000)]))
end_time_list = time.time() - start_time_list
print(f'Processing with list: {end_time_list}')

start_time_generator = time.time()
print(sum(i for i in range(100000000)))
end_time_generator = time.time() - start_time_generator
print(f'Processing with generator: {end_time_generator}')