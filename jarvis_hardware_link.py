import os

class HardwareLink:
    def __init__(self):
        self.master = "Deepak sir"
        # Oppo Reno 12 Pro sensor paths
        self.battery_path = "/sys/class/power_supply/battery/capacity"
        self.temp_path = "/sys/class/thermal/thermal_zone0/temp"

    def run_diagnosis(self):
        try:
            with open(self.battery_path, 'r') as b, open(self.temp_path, 'r') as t:
                capacity = b.read().strip()
                temp = int(t.read()) / 1000
            
            print(f"\033[1;36m[SYSTEM DIAGNOSTIC]\033[0m")
            print(f" > Battery Level: {capacity}%")
            print(f" > Core Temperature: {temp}°C")
            
            if temp > 40:
                print("\033[1;31m[ALERT]\033[0m Thermal Threshold Exceeded. Optimization Required.")
        except:
            print("\033[1;31m[ERROR]\033[0m Hardware access denied. Check Termux permissions.")

    def execute_logic(self):
        os.system('clear')
        self.run_diagnosis()
        msg = f"{self.master}, hardware link is active. I am now monitoring your Oppo Reno 12 Pro from within."
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    HardwareLink().execute_logic()
