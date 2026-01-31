from weather import weather_lookup
def main():
    city_name = input("What city would you like the weather for? ")
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
        if weather_info["code"] == "Connection":
            print("Connection error! Check that your internet is working :)")
if __name__ == "__main__":
    main()