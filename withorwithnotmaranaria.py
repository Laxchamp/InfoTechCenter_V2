# Weather Branch

import random

def get_weather():
    weather_conditions = [
        "Sunny",
        "Cloudy",
        "Rainy",
        "Foggy",
        "Snowy",
        "Stormy"
    ]
    return random.choice(weather_conditions)

def car_speed_decision(speed_limit):
    weather = get_weather()

    # Speed adjustments based on weather
    weather_speed_rules = {
        "Sunny": 1.0,     # 100% of speed limit
        "Cloudy": 0.9,    # 90%
        "Rainy": 0.7,     # 70%
        "Foggy": 0.6,     # 60%
        "Snowy": 0.4,     # 40%
        "Stormy": 0.3     # 30%
    }

    allowed_speed = int(speed_limit * weather_speed_rules[weather])

    # Car "talking"
    print("Car:", "Checking weather conditions...")
    print("Weather:", weather)

    if weather_speed_rules[weather] < 0.6:
        print("Car:", "Conditions are rough. Slowing down for safety.")
    elif weather_speed_rules[weather] < 1.0:
        print("Car:", "Not perfect weather. Driving carefully.")
    else:
        print("Car:", "Great conditions! Driving at full speed.")

    print(f"Car: Maximum safe speed is {allowed_speed} mph\n")

    return allowed_speed

# Example usage
SPEED_LIMIT = 60
car_speed_decision(SPEED_LIMIT)