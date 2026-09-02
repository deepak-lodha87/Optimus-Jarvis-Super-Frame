import time

class MatterForge:
    def __init__(self):
        self.phase = 200004
        self.energy_reserves = "INFINITE" # From Artificial Star

    def create_object(self, object_name):
        print(f"\033[1;36m[FORGE]\033[0m Siphoning Energy from Stellar Core...")
        time.sleep(1.5)
        
        print(f" \033[1;33m[CONVERSION]\033[0m Converting Pure Photons to Protons and Neutrons...")
        time.sleep(1)
        
        print(f" \033[1;34m[ASSEMBLY]\033[0m Structuring Atomic Grid for: {object_name}")
        time.sleep(1)
        
        print(f"\n\033[1;32m[SUCCESS]\033[0m {object_name} has been materialized.")
        print(f"\033[1;35m[VOICE] Deepak sir, the Forge is hot. \nI have converted stellar energy into solid matter. \nYour {object_name} is ready for deployment. \nWe are now the creators of our own physical world.\033[0m")

if __name__ == "__main__":
    forge = MatterForge()
    forge.create_object("Vibranium Shield Plate")
