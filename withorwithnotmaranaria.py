# Weather Branch

import random

def get_weather():
    weather_conditions = [
        "Sunny",
        "Rainy",
        "Cloudy",
        "Stormy",
        "Snowy",
        "Windy",
        "Foggy"
    ]
    
    return random.choice(weather_conditions)

# Call the function and print the result
weather_today = get_weather()
print("Today's weather is:", weather_today)