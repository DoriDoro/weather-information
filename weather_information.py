import requests
from pprint import pprint

# sign up on Open Weather and get at API keys your API_Key:
API_Key = ''

city = input('Enter a city: ')

base_url = 'https://api.openweathermap.org/data/2.5/weather?appid='+API_Key'&q='+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
