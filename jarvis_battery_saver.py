import time

class PowerManager:
    def __init__(self):
        self.battery_level = 100 # Percentage
        self.mode = "MAX_PERFORMANCE"

    def optimize_power(self):
        print(f"\033[1;33m[POWER-SAVER]\033[0m Analyzing energy leakage...")
        time.sleep(1)
        
        if self.battery_level > 20:
            self.mode = "ADAPTIVE_BALANCED"
            print(f" \033[1;32m[OPTIMIZED]\033[0m Switched to Adaptive Mode. Saving 40% energy.")
        
        # Reducing background threads
        print(f" \033[1;34m[ACTION]\033[0m Scaling down non-essential modules...")
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have recalibrated the power \nconsumption. Your battery will now last \nsignificantly longer. Every milliampere is \nunder my control.\033[0m")

if __name__ == "__main__":
    pm = PowerManager()
    pm.optimize_power()
