import random

def get_weather():
    return random.choice([
        "Sunny",
        "Cloudy",
        "Rainy",
        "Foggy",
        "Snowy",
        "Stormy"
    ])

def send_phone_alert(message):
    # Simulated phone message
    print("\n📱 PHONE ALERT:")
    print(message)
    print("📱 END ALERT\n")

def car_speed_decision(speed_limit, normal_travel_time):
    weather = get_weather()

    weather_rules = {
        "Sunny": 1.0,
        "Cloudy": 0.9,
        "Rainy": 0.7,
        "Foggy": 0.6,
        "Snowy": 0.4,
        "Stormy": 0.3
    }

    slowdown_factor = weather_rules[weather]
    allowed_speed = int(speed_limit * slowdown_factor)

    print("Car: Checking weather conditions...")
    print("Weather:", weather)

    # Calculate extra travel time
    adjusted_travel_time = int(normal_travel_time / slowdown_factor)
    extra_minutes = adjusted_travel_time - normal_travel_time

    if slowdown_factor < 0.6:
        print("Car: Dangerous conditions detected.")
        send_phone_alert(
            f"Bad weather ({weather}) detected.\n"
            f"Leave {extra_minutes} minutes earlier.\n"
            f"Recommended max speed: {allowed_speed} mph."
        )
    elif slowdown_factor < 1.0:
        print("Car: Conditions not ideal. Driving carefully.")
    else:
        print("Car: Weather is great. Normal driving.")

    print(f"Car: Max safe speed = {allowed_speed} mph")
    print(f"Car: Estimated travel time = {adjusted_travel_time} minutes")

# Example values
SPEED_LIMIT = 60          # mph
NORMAL_TRAVEL_TIME = 30   # minutes

car_speed_decision(SPEED_LIMIT, NORMAL_TRAVEL_TIME)