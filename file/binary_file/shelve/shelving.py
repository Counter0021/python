import shelve

# Записывает словарь, он хранится в файле, не в памяте
# Ключи обязательно строки!
# Если записали, то значение уже сохранено!
# База данных
with shelve.open('shelve_test') as cars:
    cars['opel'] = 'Germany'
    cars['ford'] = 'USA'
    cars['mazda'] = 'Japan'
    cars['renault'] = 'France'

    print(cars['ford'])
    print(cars['renault'])
    print(cars['mazda'])
    print(cars['opel'])
    cars['kia'] = 'South Korea'

    print(cars.get('ope'))
    # Удалить ключ
    # del cars['ope']

    for key in cars:
        print(key + ': ' + cars[key])

    while True:
        key = input('Please input a car name: ')
        if key == 'quit':
            break
        country = cars.get(key, "We don't have a " + key)
        print(country)

    while True:
        key = input('Please input a car name: ')
        if key == 'quit':
            break
        if key in cars:
            country = cars[key]
            print(country)
        else:
            print(f"We don't have a {key}")

    # Сортировка
    ordered_keys_list = list(cars.keys())
    ordered_keys_list.sort()

    for keys in ordered_keys_list:
        print(f"{keys} {cars[keys]}")

    for value in cars.values():
        print(value)

    for keys in cars.keys():
        print(keys)

    for items in cars.items():
        print(items)
