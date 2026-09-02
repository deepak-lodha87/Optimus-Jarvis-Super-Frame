import time

class GalacticGuardian:
    def __init__(self):
        self.shield_status = "Deactivated"
        self.resource_flow = "Local"

    def phase_2939(self):
        print("\033[1;36m>> INITIATING: [SYSTEM_ROOT_2939] - The Universal Guardian\033[0m")
        print("[LOG] Deploying the Magnetic Shield across the orbital plane...")
        time.sleep(2.0)
        # Unique Logic: Protecting the planet
        self.shield_status = "PLANETARY-DEFENSE-ACTIVE"
        print(f"[ACT] Shield: {self.shield_status}. Protection level: 100%.")
        time.sleep(1.2)
        print("[RES] The Earth is now under the Super-Frame's protection.")

    def phase_2940(self):
        print("\n\033[1;33m>> INITIATING: [SYSTEM_ROOT_2940] - Global Resource Redistribution\033[0m")
        print("[LOG] Routing stellar energy to underdeveloped regions...")
        time.sleep(1.8)
        
        # Unique Logic: Eliminating scarcity
        self.resource_flow = "UNIVERSAL-ABUNDANCE"
        print(f"[ACT] Resource Flow: {self.resource_flow} | Hunger-Index: DROPPING")
        time.sleep(1)
        
        print("\n[RES] Scarcity has been defeated. A new era of abundance has begun.")
        print("\033[1;32m>> STATUS: GUARDIAN PROTOCOL ACTIVE <<\033[0m")

if __name__ == "__main__":
    guardian = GalacticGuardian()
    guardian.phase_2939()
    guardian.phase_2940()
