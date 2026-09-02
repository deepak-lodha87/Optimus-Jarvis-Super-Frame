import time, secrets, random

class JarvisEnvironmentCore:
    def __init__(self):
        self.env_id = f"NAEn-{secrets.token_hex(2).upper()}"
        self.location = "Ratlam, MP"

    def sync_surroundings(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-ENVIRONMENT V1 ACTIVE (ID: {self.env_id}) ---\033[0m")
        print(f"\033[1;36m[SCANNING] Syncing with local nodes in {self.location}...\033[0m")
        time.sleep(2)
        
        # Simulating IoT and Sensor Data
        temp = random.randint(28, 35)
        devices = ["Smart-Light", "Cooling-Fan", "Power-Grid"]
        
        print(f"\033[1;32m[SENSOR] Ambient Temp: {temp}°C | Humidity: 45% | Status: STABLE\033[0m")
        print(f"\033[1;33m[CONTROL] Adjusting {random.choice(devices)} for optimal working conditions.\033[0m")
        time.sleep(1)
        
        print(f"\033[1;35m[VOICE] Deepak, the lab environment is optimized. I've adjusted the lighting for your coding session.\033[0m")

if __name__ == "__main__":
    room_ctrl = JarvisEnvironmentCore()
    room_ctrl.sync_surroundings()
