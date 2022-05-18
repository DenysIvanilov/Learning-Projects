import requests

API = "ebf05b9661c529a5d1a0e8ce63c381bf"

while True:
    city = input("Enter city: ")
    if len(city) < 1:
        print("You didn't enter the city")
        break
    country_code = input("Enter a country code(optional): ")
    units = input("Enter units of measurement(imperial or metric),otherwise it is Kelvin by default: ")
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country_code + "&units=" + units + \
          "&appid=" + API
    data = requests.get(url).json()
    if data["cod"] != 200:
        print("Such city probably doesn't exist or you didn't enter everything correctly. Try one more time")
        break
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    wind = data["wind"]["speed"]
    print(f"The weather is {weather}\n"
          f"Temperature is {temp}\n"
          f"The speed of wind is {wind}")
    done = input("Do you want to continue?(y/n): ").lower()
    if done.startswith("y"):
        continue
    else:
        break






