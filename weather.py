import json
import requests
from config import WEATHER_API_KEY
def weather_lookup(city):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=imperial") #making API request
    except requests.exceptions.RequestException:
        return {"error": True, "code": "Connection"}
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
if __name__ == "__main__":
    weather_lookup()