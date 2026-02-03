
# BetaTestDev Branch

# Welcome Branch
# This program simulates a colorful OS-style boot screen

# Libraries Imported Here
import sys      # Lets us control terminal output
import time     # Lets us add delays for animation timing
import os       # Used to enable ANSI color support on Windows

# Enable ANSI escape codes on Windows terminals
# (Does nothing on Mac/Linux, safe to include)
os.system("")

# ANSI color codes for terminal text coloring
RESET   = "\033[0m"   # Resets text back to normal color
GREEN   = "\033[92m"  # Bright green text
CYAN    = "\033[96m"  # Bright cyan text
YELLOW  = "\033[93m"  # Bright yellow text
MAGENTA = "\033[95m"  # Bright magenta text

# Print the title lines in color
print(f"\n{MAGENTA}Welcome Branch - Developer Cole{RESET}")
print(f"\n{CYAN}Welcome to InfoTechCenter V.1.0{RESET}")

# x controls how long the boot loop runs
x = 0

# ellipsis controls how many dots appear after "Booting"
ellipsis = 0

# Main boot animation loop
# Runs until x reaches 20 cycles
while x != 20:
    x += 1  # Increase loop counter each cycle

    # Build the boot message with a growing number of dots
    ellipsisMessage = f"{YELLOW}InfoTechCenter OS Booting{'.' * ellipsis}{RESET}"
    ellipsis += 1  # Increase dot count each loop

    # Write the message on the same line (\r returns cursor to line start)
    # \033[K clears the rest of the line
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()  # Forces the text to appear immediately

    # Pause to create animation timing
    time.sleep(.5)

    # Reset dots after 3 so it cycles "...", then starts over
    if ellipsis == 4:
        ellipsis = 0

    # When loop finishes, print the success message
    if x == 20:
        print(f"\n{GREEN}Operating System Booted Up - Retina Access Granted{RESET}")



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


# Gasoline Branch
# This program simulates checking a car's gas level and deciding
# whether we need to stop for gas before a trip.

import random  # Used to generate random gas levels for simulation

# ----------------------------
# 1. Determine gas level
# ----------------------------

# The maximum amount of gas the car's tank can hold (in gallons)
TANK_CAPACITY = 15  

# Randomly generate the current amount of gas in the tank
# random.uniform(1, 15) gives a decimal number between 1 and 15
# round(..., 2) rounds the number to 2 decimal places
gas_in_tank = round(random.uniform(1, 15), 2)

# Display the current gas level to the user
print(f"⛽ Current gas level: {gas_in_tank} gallons")

# ----------------------------
# 2. Check if gas is below 1/4 tank
# ----------------------------

# Calculate what one-quarter of the tank is
QUARTER_TANK = TANK_CAPACITY * 0.25

# Determine if the current gas level is at or below 1/4 tank
# This creates a Boolean (True or False) value
need_gas = gas_in_tank <= QUARTER_TANK

# Output a message based on whether gas is needed
if need_gas:
    print("⚠️ Gas is below 1/4 tank. You need gas!")
else:
    print("✅ Gas level is fine.")

# ----------------------------
# 3. List of gas stations
# ----------------------------

# A list of dictionaries, where each dictionary represents a gas station
# Each station includes:
# - name: station name
# - distance: miles away from the car
# - price: cost per gallon
# - open: whether the station is open
# - snacks: whether the station sells snacks
gas_stations = [
    {"name": "Shell", "distance": 5, "price": 3.59, "open": True, "snacks": True},
    {"name": "BP", "distance": 8, "price": 3.45, "open": True, "snacks": False},
    {"name": "Speedway", "distance": 3, "price": 3.69, "open": False, "snacks": True},
    {"name": "Mobil", "distance": 6, "price": 3.49, "open": True, "snacks": True}
]

# ----------------------------
# 4. Find cheapest gas station
# ----------------------------

# Create a new list that only includes gas stations that are open
# This uses a list comprehension for filtering
open_stations = [s for s in gas_stations if s["open"]]

# Find the cheapest station from the open stations list
# The key parameter tells min() to compare stations by gas price
cheapest_station = min(open_stations, key=lambda s: s["price"])

# Display the cheapest open gas station
print(f"\n💰 Cheapest open station: {cheapest_station['name']} at ${cheapest_station['price']}")

# ----------------------------
# 5. Can we make it there?
# ----------------------------

# Miles per gallon the car can travel
MPG = 25  

# Calculate the maximum distance the car can travel
max_distance = gas_in_tank * MPG

# Check if the car can reach the cheapest gas station
if max_distance >= cheapest_station["distance"]:
    can_make_it = True
    print("🚗 You can make it to the gas station.")
else:
    can_make_it = False
    print("❌ You cannot make it to the gas station!")

# ----------------------------
# 6. Snacks check
# ----------------------------

# Check whether the selected gas station has snacks
if cheapest_station["snacks"]:
    print("🍿 Snacks available!")
else:
    print("🚫 No snacks available.")

# ----------------------------
# 7. Update alarm if gas is needed
# ----------------------------

# Function that simulates updating a morning alarm
# This would normally connect to a phone or alarm app
def update_alarm():
    print("\n⏰ Alarm updated: Wake up earlier to get gas!")

# Decide whether to update the alarm based on gas and reachability
if need_gas and can_make_it:
    update_alarm()
elif need_gas and not can_make_it:
    print("\n🚨 WARNING: You may run out of gas before reaching a station!")

