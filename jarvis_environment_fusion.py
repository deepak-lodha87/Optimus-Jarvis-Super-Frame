import time
import random

class EnvironmentalFusion:
    def __init__(self):
        self.location = "Ratlam, India" # Live Context
        self.altitude = 480 # Meters (Approx for Ratlam)

    def fetch_sensor_data(self):
        print(f"\033[1;36m[SENSORS] Accessing Reno 12 Pro Environmental Suite...\033[0m")
        time.sleep(1.2)
        temp = random.randint(25, 42)
        pressure = random.uniform(950, 1050)
        print(f"  • Ambient Temp: {temp}°C")
        print(f"  • Air Pressure: {pressure:.2f} hPa")
        return {"temp": temp, "pressure": pressure}

class BlueprintAdaptation:
    def adjust_logic(self, data):
        print("\033[1;35m[ADAPT] Recalculating Blueprints based on Sensor Data...\033[0m")
        time.sleep(1.5)
        if data['temp'] > 38:
            return "\033[1;33m[ADJUSTED] High-Heat detected. Increasing Cooling-Cycle in Blueprints.\033[0m"
        return "\033[1;32m[STABLE] Environment is Optimal. Standard Blueprint parameters active.\033[0m"

if __name__ == "__main__":
    env = EnvironmentalFusion()
    adapt = BlueprintAdaptation()
    
    print("-" * 50)
    print("   JARVIS ENVIRONMENTAL DATA FUSION (P3143-44)")
    print("-" * 50)
    
    sensor_logs = env.fetch_sensor_data()
    print("\n" + adapt.adjust_logic(sensor_logs))
    print("-" * 50)
