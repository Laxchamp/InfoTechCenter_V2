# Gasoline Branch
import random

# ----------------------------
# 1. Determine gas level
# ----------------------------

TANK_CAPACITY = 15  # gallons
gas_in_tank = round(random.uniform(1, 15), 2)

print(f"⛽ Current gas level: {gas_in_tank} gallons")

# ----------------------------
# 2. Check if gas is below 1/4 tank
# ----------------------------

QUARTER_TANK = TANK_CAPACITY * 0.25
need_gas = gas_in_tank <= QUARTER_TANK

if need_gas:
    print("⚠️ Gas is below 1/4 tank. You need gas!")
else:
    print("✅ Gas level is fine.")

# ----------------------------
# 3. List of gas stations
# ----------------------------

gas_stations = [
    {"name": "Shell", "distance": 5, "price": 3.59, "open": True, "snacks": True},
    {"name": "BP", "distance": 8, "price": 3.45, "open": True, "snacks": False},
    {"name": "Speedway", "distance": 3, "price": 3.69, "open": False, "snacks": True},
    {"name": "Mobil", "distance": 6, "price": 3.49, "open": True, "snacks": True}
]

# ----------------------------
# 4. Find cheapest gas station
# ----------------------------

open_stations = [s for s in gas_stations if s["open"]]

cheapest_station = min(open_stations, key=lambda s: s["price"])

print(f"\n💰 Cheapest open station: {cheapest_station['name']} at ${cheapest_station['price']}")

# ----------------------------
# 5. Can we make it there?
# ----------------------------

MPG = 25  # miles per gallon
max_distance = gas_in_tank * MPG

if max_distance >= cheapest_station["distance"]:
    can_make_it = True
    print("🚗 You can make it to the gas station.")
else:
    can_make_it = False
    print("❌ You cannot make it to the gas station!")

# ----------------------------
# 6. Snacks check
# ----------------------------

if cheapest_station["snacks"]:
    print("🍿 Snacks available!")
else:
    print("🚫 No snacks available.")

# ----------------------------
# 7. Update alarm if gas is needed
# ----------------------------

def update_alarm():
    print("\n⏰ Alarm updated: Wake up earlier to get gas!")

if need_gas and can_make_it:
    update_alarm()
elif need_gas and not can_make_it:
    print("\n🚨 WARNING: You may run out of gas before reaching a station!")