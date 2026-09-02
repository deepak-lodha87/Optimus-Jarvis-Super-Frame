import time
import random

class PowerManager:
    def __init__(self):
        self.battery_percent = 100
        self.estimated_flight_time = 25 # Minutes

    def monitor_power(self):
        print("\033[1;36m[POWER]\033[0m Activating Smart Energy Management...")
        time.sleep(1.2)
        
        while self.battery_percent > 15:
            # Simulating power drain based on flight conditions
            drain = random.randint(5, 10)
            self.battery_percent -= drain
            self.estimated_flight_time = (self.battery_percent / 4)
            
            print(f" \033[1;34m[BATTERY]\033[0m {self.battery_percent}% | Remaining: {round(self.estimated_flight_time, 1)} mins")
            
            if self.battery_percent < 30:
                print("  \033[1;33m[ECO-MODE]\033[0m Reducing non-essential CPU tasks to save power.")
            
            time.sleep(0.8)

        print(f"\n\033[1;31m[CRITICAL]\033[0m Battery at {self.battery_percent}%. Initiating Emergency Landing.")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am optimizing every \nmilliampere of our energy. My goal is to \nkeep us in the sky as long as possible. \nI am balancing power and performance to \nensure a safe return. Your mission is my \npriority.\033[0m")

if __name__ == "__main__":
    pm = PowerManager()
    pm.monitor_power()
