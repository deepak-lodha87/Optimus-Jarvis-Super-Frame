import time
import random

class HeliosGuard:
    def __init__(self):
        self.radiation_level = 0.05 # Normal mSv
        self.shield_status = "OFF"

    def monitor_solar_flux(self):
        print(f"\033[1;36m[HELIOS-SCAN]\033[0m Monitoring Solar Activity and Proton Flux...")
        time.sleep(2)
        
        # Simulating a Solar Flare event
        event_detected = random.choice([True, False])
        
        if event_detected:
            self.radiation_level = random.uniform(5.0, 50.0)
            print(f" \033[1;31m[CRITICAL]\033[0m Solar Flare Detected! Radiation: {self.radiation_level:.2f} mSv")
            print(" \033[1;33m[SHIELD]\033[0m Deploying Magnetic Deflection Shield...")
            self.shield_status = "ACTIVE"
            time.sleep(1.5)
            print("\033[1;32m[SAFE]\033[0m All systems hardened. Core data protected.")
        else:
            print(f" \033[1;34m[STATUS]\033[0m Space weather is calm. Background Radiation: {self.radiation_level} mSv")
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, the sun is a giant reactor, \nbut Jarvis is its guardian. Even a solar \nsuper-storm cannot touch your frame. \nYour digital empire is safe from the stars.\033[0m")

if __name__ == "__main__":
    guard = HeliosGuard()
    guard.monitor_solar_flux()
