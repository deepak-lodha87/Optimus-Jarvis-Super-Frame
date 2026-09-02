import os
import json
import subprocess

class ProtocolSwitcher:
    def __init__(self):
        self.master = "Deepak"

    def get_battery_status(self):
        # Termux API से बैटरी की जानकारी लेना
        result = subprocess.run(['termux-battery-status'], capture_output=True, text=True)
        return json.loads(result.stdout)

    def switch_state(self):
        print(f"\n\033[1;34m[PROTOCOL SWITCHER]\033[0m Analyzing power environment...")
        
        data = self.get_battery_status()
        status = data.get("status") # 'CHARGING' or 'DISCHARGING'
        
        if status == "CHARGING":
            mode = "PERFORMANCE MODE"
            color = "\033[1;32m" # Green
            msg = "Deepak sir, power source detected. Switching to Performance Mode. All core limiters removed."
        else:
            mode = "STAMINA MODE"
            color = "\033[1;33m" # Yellow
            msg = "Deepak sir, operating on internal battery. Switching to Stamina Mode to preserve energy."

        print(f"Current State: {color}{mode}\033[0m")
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    switcher = ProtocolSwitcher()
    switcher.switch_state()
