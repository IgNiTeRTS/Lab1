import requests
city = 'Moscow,Ru'
appid = '9c2f430202b8b246469b368dc5b1057c'

res = requests.get("http://api.openweathermap.org/data/2.5/weather",params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()