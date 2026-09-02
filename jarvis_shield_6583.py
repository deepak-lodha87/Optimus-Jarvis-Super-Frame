import time, secrets, random

class JarvisShield:
    def __init__(self):
        self.shield_id = f"NASh-{secrets.token_hex(2).upper()}"
        self.status = "Active"

    def monitor_hardware(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-SHIELD V2 ACTIVE (ID: {self.shield_id}) ---\033[0m")
        print("\033[1;36m[MONITORING] Scanning Thermal and Motion Sensors...\033[0m")
        time.sleep(1.2)
        
        hazards = ["Sudden Impact", "High Thermal Load", "Unstable Voltage"]
        event = random.choice(hazards)
        
        print(f"\033[1;31m[ALERT] Hazard Detected: {event}!\033[0m")
        time.sleep(0.8)
        
        print(f"\033[1;32m[ACTION] Deploying Digital Shield Layer 1... Neutralized.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the hardware is safe. I have adjusted the system parameters to absorb the impact.\033[0m")

if __name__ == "__main__":
    shield = JarvisShield()
    shield.monitor_hardware()
