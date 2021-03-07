# Землетрясения
import requests

url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"

starttime = input('Enter the start time: ')
endtime = input('Enter the end time: ')
latitude = input('Enter the latitude: ')
longitude = input('Enter the longitude: ')
maxradiuskm = input('Enter the max radius in km: ')
minmagnitude = input('Enter the min magnitude: ')

response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'geojson',
    'starttime': starttime,
    'endtime': endtime,
    'latitude': latitude,
    'longitude': longitude,
    'maxradiuskm': maxradiuskm,
    'minmagnitude': minmagnitude
})

data = response.json()

for i in range(len(data['features'])):
    print(f"{i}. Place: {data['features'][i]['properties']['place']}. Magnitude: {data['features'][i]['properties']['mag']}")