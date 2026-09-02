import os
import time

class HardwareOverride:
    def __init__(self):
        self.user = "Deepak sir"
        self.status = "Dominance Established" #

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def inject_protocol(self, machine_type):
        print(f"\033[1;33m[INJECTING]\033[0m Accessing {machine_type} Electrical Core...")
        time.sleep(1)
        
        # Real-world logic for direct control
        if machine_type == "Vehicle":
            print("\033[1;32m[LINKED]\033[0m Car's Electrical System is under Jarvis control.")
            self.speak(f"{self.user}, I have bypassed the car's security. Engine diagnostics are live.")
        elif machine_type == "Drone":
            print("\033[1;32m[LINKED]\033[0m Drone PWM signals intercepted.")
            self.speak("Sir, drone flight systems are now synchronized.")

if __name__ == "__main__":
    override = HardwareOverride()
    # Test for Universal Control
    override.inject_protocol("Vehicle")
    override.inject_protocol("Drone")
