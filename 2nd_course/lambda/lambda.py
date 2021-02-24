import time

# Обычная
#def gms():
#    return int(time.time() % 1 * 1000)

# lambda (анонимная)
gms = lambda : int(time.time() % 1 * 1000)

print(gms())