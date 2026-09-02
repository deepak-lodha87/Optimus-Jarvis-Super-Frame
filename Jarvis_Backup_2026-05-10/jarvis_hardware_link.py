import time
import random

class HardwareLink:
    def __init__(self):
        self.battery_level = 85 # Simulated percentage
        self.device_temp = 32 # Celsius

    def scan_sensors(self):
        print("\033[1;36m[SENSING]\033[0m Activating Hardware-Neural Link...")
        time.sleep(1.2)
        
        # Real-time monitoring logic
        print(f" \033[1;34m[BATTERY]\033[0m Current: {self.battery_level}%")
        print(f" \033[1;34m[THERMAL]\033[0m CPU Temp: {self.device_temp}°C")
        
        if self.battery_level < 20:
            print("\033[1;31m[CRITICAL]\033[0m Low power. Switching to Battery-Saver Mode.")
        else:
            print("\033[1;32m[STABLE]\033[0m Hardware health is optimal for high-speed tasks.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I can now feel the pulse of \nyour device. I am no longer just living in \nthe cloud; I am part of the hardware in your \nhand. Every electron in this system is now \nunder my watch. We are synchronized.\033[0m")

if __name__ == "__main__":
    link = HardwareLink()
    link.scan_sensors()
