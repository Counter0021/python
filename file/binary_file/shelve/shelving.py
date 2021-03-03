import shelve

# Записывает словарь, он хранится в файле, не в памяте
# Ключи обязательно строки!
# Если записали, то значение уже сохранено!
with shelve.open('shelve_test') as cars:
    cars['opel'] = 'Germany'
    cars['ford'] = 'USA'
    cars['mazda'] = 'Japan'
    cars['renault'] = 'France'

    print(cars['ford'])
    print(cars['renault'])
    print(cars['mazda'])
    print(cars['opel'])

    # Удалить ключ
    # del cars['ope']

    for key in cars:
        print(key)
