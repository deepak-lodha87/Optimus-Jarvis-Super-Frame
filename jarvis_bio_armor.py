import time
import random

class BioArmorSystem:
    def __init__(self):
        self.armor_density = "Soft"
        self.health_status = "Optimal"

    def detect_impact(self):
        print(f"\033[1;36m[BIO-SHIELD]\033[0m Monitoring Sub-Dermal Mesh integrity...")
        time.sleep(1.5)
        
        # Simulating a physical threat
        threat_level = random.randint(1, 100)
        
        if threat_level > 70:
            print(f" \033[1;31m[WARNING]\033[0m Physical Impact Detected! Level: {threat_level}")
            self.armor_density = "Solid-State Titanium-Grade"
            print(f" \033[1;32m[ACTION]\033[0m Nano-Armor Hardened. Energy Absorbed.")
        else:
            print(f" \033[1;34m[STATUS]\033[0m Normal activity. Mesh remains flexible.")

        print(f"\n\033[1;35m[VOICE] Deepak sir, I am now your second skin. \nI will absorb every blow and heal every \nscratch before you even feel it. You are \nphysically fortified.\033[0m")

if __name__ == "__main__":
    armor = BioArmorSystem()
    armor.detect_impact()
