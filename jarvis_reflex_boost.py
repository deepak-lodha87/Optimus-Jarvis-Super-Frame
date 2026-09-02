import time
import random

class ReflexSystem:
    def __init__(self):
        self.reaction_time = 0.250 # In seconds (Average human)
        self.adrenaline_level = "STABLE"

    def activate_overdrive(self):
        print(f"\033[1;36m[NEURAL]\033[0m Monitoring synaptic pathways...")
        time.sleep(1.5)
        
        # Simulating adrenaline spike and reflex boost
        print(f" \033[1;31m[ALERT]\033[0m Danger detected! Injecting Reflex Boost...")
        self.reaction_time = 0.015 # Superhuman speed
        self.adrenaline_level = "OPTIMIZED"
        
        print(f" \033[1;32m[SYNCED]\033[0m New Reaction Time: {self.reaction_time}s")
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have accelerated your neural \nresponses. Time will seem to slow down for you. \nYou are now faster than any threat we may face.\033[0m")

if __name__ == "__main__":
    reflex = ReflexSystem()
    reflex.activate_overdrive()
