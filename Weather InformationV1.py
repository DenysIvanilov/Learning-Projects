import requests


API = "ebf05b9661c529a5d1a0e8ce63c381bf"

city = input("Enter city: ")
country_code = input("Enter a country code: ")

geocode_url = "http://api.openweathermap.org/geo/1.0/direct?q=" + city + "," + country_code + "&limit=1&appid=" + API

data = requests.get(geocode_url).json()

lat = data[0]["lat"]
lon = data[0]["lon"]

weather_url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&units=metric&appid=" + API

weather = requests.get(weather_url).json()

temp = weather["main"]["temp"]
main = weather["weather"][0]["main"]
desc = weather["weather"][0]["description"]

print(f"The weather is {main} - {desc} with a temperature of {temp} Celsius")



