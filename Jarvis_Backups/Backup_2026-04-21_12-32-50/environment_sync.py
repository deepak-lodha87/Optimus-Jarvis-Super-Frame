import time

class EnvironmentalCore:
    def __init__(self, location):
        self.location = location
        self.data_source = "Orbital Satellite Link"

    def phase_2601(self):
        print(f"\033[1;36m>> INITIATING: [SYSTEM_ROOT_2601] - Location Sync\033[0m")
        print(f"[LOG] Detecting current coordinates...")
        time.sleep(1.2)
        print(f"[RES] Location Identified: {self.location}. Syncing with {self.data_source}.")

    def phase_2602(self):
        print("\n\033[1;33m>> INITIATING: [SYSTEM_ROOT_2602] - Climate Analysis\033[0m")
        print("[LOG] Fetching real-time atmospheric data...")
        time.sleep(1.5)
        # Unique Logic: Dynamic weather report simulation
        weather_data = {"Temp": "38°C", "Condition": "Sunny/Clear", "Humidity": "20%"}
        print(f"[ACT] Processing: Temperature {weather_data['Temp']} | {weather_data['Condition']}")
        print(f"[RES] Environment Data Logged. Jarvis is now aware of your surroundings.")
        print("\033[1;32m>> STATUS: CONTEXTUAL AWARENESS ACTIVE\033[0m")

if __name__ == "__main__":
    # Setting location to Ratlam based on your current stay
    env = EnvironmentalCore("Ratlam, MP")
    env.phase_2601()
    env.phase_2602()
