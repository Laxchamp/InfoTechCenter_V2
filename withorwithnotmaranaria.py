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