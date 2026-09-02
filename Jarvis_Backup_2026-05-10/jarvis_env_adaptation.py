import time
import random

class EnvironmentalJarvis:
    def __init__(self):
        self.user = "Deepak"
        self.phase = "3047"
        self.modes = ["Study Mode", "Combat Prep", "Restoration"]

    def scan_surroundings(self):
        print(f"\033[1;35m>> PHASE {self.phase}: SCANNING PHYSICAL ENVIRONMENT <<\033[0m")
        time.sleep(1)
        # Simulating sensor data from the room
        light_level = random.randint(200, 800) # Lumens
        temp = random.uniform(22.0, 28.5) # Celsius
        print(f"\033[1;34m[ENV] Light: {light_level}lx | Temperature: {temp:.1f}°C\033[0m")
        return light_level, temp

    def optimize_space(self, light, temp):
        print("\033[1;36m[ACTION] Synchronizing Workspace for Architect Deepak... <<\033[0m")
        time.sleep(1)
        if light < 400:
            print("\033[1;33m[ADJUST] Low light detected. Increasing HUD brightness & virtual lamp.\033[0m")
        if temp > 26.0:
            print("\033[1;33m[ADJUST] Temperature rising. Activating internal suit cooling simulation.\033[0m")
        
        print("\033[1;32m[SUCCESS] Environment Optimized for 'Deep Work' Protocol.\033[0m")

    def run(self):
        print(f"\033[1;32m>> SENSORY GRID ACTIVE: JARVIS IS BALANCING YOUR SURROUNDINGS. <<\033[0m")
        l, t = self.scan_surroundings()
        self.optimize_space(l, t)

if __name__ == "__main__":
    env_system = EnvironmentalJarvis()
    env_system.run()
