import requests

Weather_key = "a60fbc50b3bac25e8a5691f8340403a9"
base_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{base_url}?appid={Weather_key}&q={city}"
data = requests.get(request_url)

if data.status_code == 200:
    information = data.json()
    weather = information['weather'][0]['description']
    temperature = round(information['main']['temp'] - 273.15, 2)
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occured")
