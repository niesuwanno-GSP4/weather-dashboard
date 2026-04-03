import requests
import json

API_KEY = "ใส่_API_ของคุณตรงนี้"
CITY = "Bangkok"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

res = requests.get(url)
data = res.json()

temp = data['main']['temp']
humidity = data['main']['humidity']

heat_index = temp + 0.33*humidity/100*6 - 4

status = "Safe"
if heat_index > 40:
    status = "Danger"
elif heat_index > 35:
    status = "Caution"

output = {
    "temp": temp,
    "humidity": humidity,
    "heat_index": round(heat_index,1),
    "status": status
}

with open('data/weather.json', 'w') as f:
    json.dump(output, f)
