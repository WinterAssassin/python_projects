import requests
from datetime import datetime

URL = 'https://api.sunrise-sunset.org/json'

MY_LAT = 12.879721
MY_LONG = 121.774017

parameters = {
    'lat': MY_LAT,
    'long': MY_LONG,
    'formatted': 0,
}

response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)