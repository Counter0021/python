# Погода
import requests

url = 'https://api.weatherbit.io/v2.0/current?'
apiKey = 'a1f7055ff16b4670ad4f977de4b28fdb'
print('Please write only in English! If there are no values, the default values will be used.')
language = input('Enter language(first 2 letter) or default language - english: ').lower()
city = input('Enter city: ').lower() or 'krasnodar'
country = input('Enter country: ').lower() or 'russia'

response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'key': apiKey,
    'lang': language,
    'city': city,
    'country': country
})

data = response.json()
# Сократить запись
data_def = data['data'][0]
# Время последнего обновления погоды
date_lat_update = data_def['ob_time']
# Нормальное время
date_lat_update_1 = f'{date_lat_update[8:10]}-{date_lat_update[5:8]}{date_lat_update[0:4]} ' \
                    + date_lat_update[11:]
name_city = data_def['city_name']

print(
    f"Weather in {country.upper()} {name_city} is {data_def['weather']['description'].lower()}. " \
    + f"Latest weather update: {date_lat_update_1}.")
print(f"Located at latitude: {round(data_def['lat'])} and longitude: {round(data_def['lon'])}.")
print(f"Temperature in {name_city}: {data_def['temp']} C. Feels like: {data_def['app_temp']} C.")
print(f"""Sunrise time: {data_def['sunrise']}.
Sunset time: {data_def['sunset']}.
Verbal wind direction: {data_def['wind_cdir_full']}.""")
