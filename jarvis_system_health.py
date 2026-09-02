import os
import time

class SystemMonitor:
    def __init__(self):
        self.master = "Deepak"

    def check_vitals(self):
        print(f"\n\033[1;36m[SYSTEM SCAN]\033[0m Monitoring Hardware Vitals for {self.master} sir...")
        
        # बैटरी लेवल प्राप्त करना (Termux API की मदद से)
        battery_data = os.popen("termux-battery-status").read()
        
        # बैटरी प्रतिशत निकालना
        import json
        data = json.loads(battery_data)
        percentage = data['percentage']
        status = data['status']
        temp = data['temperature']

        print(f"\n\033[1;32mBattery:\033[0m {percentage}%")
        print(f"\033[1;32mStatus:\033[0m {status}")
        print(f"\033[1;32mTemp:\033[0m {temp}°C")

        # चेतावनी का लॉजिक (Critical Alerts)
        if percentage < 20:
            msg = f"Warning Deepak sir! Power levels are critical at {percentage} percent. Please connect the energy cell."
            print("\033[1;31m[LOW POWER ALERT]\033[0m")
        elif temp > 40:
            msg = f"System alert! Core temperature is rising. Current thermal level: {temp} degrees. Initiating cooling sequence."
            print("\033[1;31m[OVERHEAT ALERT]\033[0m")
        else:
            msg = f"Systems are nominal sir. Battery is at {percentage} percent and temperature is stable."

        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.check_vitals()
