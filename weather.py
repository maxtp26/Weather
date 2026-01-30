import json
import requests
def weather_lookup(city):
    from config import WEATHER_API_KEY
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=imperial") #making API request
    status = response.status_code
    data = response.json() #converting to dictionary from json
    if status == 200: #checking that server doesn't return error
        if "main" in data and "weather" in data and "wind" in data: #checking all these keys actually exist
            main = data["main"]
            weather = data["weather"][0]
            wind = data["wind"]
            if "temp" in main:
                temp = main["temp"]
            else:
                temp = "missing temperature data"
            if "main" in weather:
                weather_status = weather["main"]
            else:
                weather_status = "missing weather data"
            if "speed" in wind:
                wind_speed = wind["speed"]
            else: 
                wind_speed = "missing wind data"
            if "humidity" in main:
                humidity = main["humidity"]
            else:
                humidity = "missing humidity data"
            weather_dict = {"error": False,"temp": temp, "status": weather_status, "wind": wind_speed, "humidity": humidity} #1 indicates to UI no errors
            return weather_dict
    else:
        if int(data["cod"]) == 404:
            return {"error": True, "code": "CNF"}
        elif int(data["cod"]) == 401:
            return {"error": True, "code": "API"}
        else:
            return {"error": True, "code": "Server"}
def main():
    city_name = input("What city would you like the weather for? ")
    try:
        weather_info = weather_lookup(city_name)
        if not weather_info["error"]:
            print(f"In {city_name}, the temperature is {weather_info["temp"]} degrees Fahrenheit. The condition is {weather_info["status"]}, with wind speeds of {weather_info["wind"]} miles per hour and {weather_info["humidity"]}% humidity.")
        else:
            if weather_info["code"] == "CNF":
                print("Invalid city! Check your spelling?")
            if weather_info["code"] == "API":
                print("Invalid API! Double check it!")
            if weather_info["code"] == "Server":
                print("Server response error! Try waiting or look at the OpenWeather website for more info.")
    except requests.exceptions.RequestException:
        print("Connection error! Is your internet working?")
main()