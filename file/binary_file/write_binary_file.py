# Запись двоичных файлов
# 'bw' - запись двоичных файлов
with open('test_binary', 'bw') as test_file:
    # test_file.write(bytes(range(21)))
    for number in range(21):
        # Нужно именно передавать в списке!
        test_file.write(bytes([number]))

# Чтение
# 'br' - чтение двоичных файлов
with open('test_binary', "br") as test_file:
    for number in test_file:
        print(number)