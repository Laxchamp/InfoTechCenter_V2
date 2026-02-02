# Import the random module so we can randomly select weather conditions
import random


# Function that randomly returns a weather condition
def get_weather():
    # random.choice picks ONE item from the list each time the function is called
    return random.choice([
        "Sunny",
        "Cloudy",
        "Rainy",
        "Foggy",
        "Snowy",
        "Stormy"
    ])


# Function that simulates sending a message to a phone
def send_phone_alert(message):
    # This is just a simulation, so we print the alert instead of actually texting
    print("\n📱 PHONE ALERT:")
    print(message)
    print("📱 END ALERT\n")


# Function that decides the car's speed and travel time based on weather
def car_speed_decision(speed_limit, normal_travel_time):
    # Get a random weather condition
    weather = get_weather()

    # Dictionary that assigns a slowdown factor to each type of weather
    # Lower numbers mean worse driving conditions
    weather_rules = {
        "Sunny": 1.0,    # No slowdown
        "Cloudy": 0.9,   # Slight slowdown
        "Rainy": 0.7,    # Moderate slowdown
        "Foggy": 0.6,    # Poor visibility
        "Snowy": 0.4,    # Very slippery
        "Stormy": 0.3    # Extremely dangerous
    }

    # Get the slowdown factor for the current weather
    slowdown_factor = weather_rules[weather]

    # Calculate the maximum allowed speed based on weather conditions
    allowed_speed = int(speed_limit * slowdown_factor)

    # Display weather information
    print("Car: Checking weather conditions...")
    print("Weather:", weather)

    # Adjust travel time based on how much slower the car must go
    adjusted_travel_time = int(normal_travel_time / slowdown_factor)

    # Calculate how many extra minutes the trip will take
    extra_minutes = adjusted_travel_time - normal_travel_time

    # If conditions are dangerous, warn the driver and send a phone alert
    if slowdown_factor < 0.6:
        print("Car: Dangerous conditions detected.")
        send_phone_alert(
            f"Bad weather ({weather}) detected.\n"
            f"Leave {extra_minutes} minutes earlier.\n"
            f"Recommended max speed: {allowed_speed} mph."
        )

    # If conditions are not perfect but still drivable
    elif slowdown_factor < 1.0:
        print("Car: Conditions not ideal. Driving carefully.")

    # If conditions are perfect
    else:
        print("Car: Weather is great. Normal driving.")

    # Display final driving recommendations
    print(f"Car: Max safe speed = {allowed_speed} mph")
    print(f"Car: Estimated travel time = {adjusted_travel_time} minutes")


# -------------------- MAIN PROGRAM --------------------

# Speed limit in miles per hour
SPEED_LIMIT = 60

# Normal travel time in minutes
NORMAL_TRAVEL_TIME = 30

# Call the function to simulate the car's decision-making
car_speed_decision(SPEED_LIMIT, NORMAL_TRAVEL_TIME)