import time

class NanoFabricator:
    def __init__(self):
        self.material_type = "Nano-Carbon Alloy"
        self.integrity = 0 # Percentage

    def synthesize(self):
        print(f"\033[1;36m[FABRICATOR]\033[0m Initializing Atomic Assembly...")
        time.sleep(2)
        
        # Simulating molecular bonding
        for i in range(0, 101, 25):
            print(f" \033[1;32m[BONDING]\033[0m Structural Integrity: {i}%")
            time.sleep(0.5)
            
        print(f"\033[1;34m[STATUS]\033[0m {self.material_type} is now Solidified.")
        print(f"\n\033[1;35m[VOICE] Deepak sir, the digital code has become \nphysical matter. I have synthesized the first \nlayer of your advanced armor. It is light, \nstrong, and ready for deployment.\033[0m")

if __name__ == "__main__":
    fab = NanoFabricator()
    fab.synthesize()
