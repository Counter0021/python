# Измерение промежутков времени
import time

input('Press ENTER to start ')

# Старт время
# start_time = time.monotonic()

# Более точный замер .perf_counter()
start_time = time.perf_counter()

x = 0
for i in range(10000000):
    x = i * i

print(x)

# Конец время
# end_time = time.monotonic()
end_time = time.perf_counter()

print(end_time - start_time)