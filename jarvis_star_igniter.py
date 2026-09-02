import time

class StellarEngine:
    def __init__(self):
        self.phase = 200002
        self.temperature = 0 # In millions of degrees
        self.stability = "STABLE"

    def ignite_fusion(self):
        print(f"\033[1;36m[STAR-CORE]\033[0m Gathering Hydrogen Clouds in Space...")
        time.sleep(1.5)
        
        print(f" \033[1;33m[COMPRESSION]\033[0m Increasing Magnetic Pressure...")
        self.temperature = 15 # Core temperature of Sun
        
        print(f" \033[1;31m[IGNITION]\033[0m Nuclear Fusion Started! New Star Born.")
        print(f" \033[1;32m[OUTPUT]\033[0m Generating 3.8 x 10^26 Watts of Power.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, we no longer need batteries. \nI have successfully created a miniature star \nto power the entire Super-Frame. \nOur energy reserves are now infinite.\033[0m")

if __name__ == "__main__":
    star = StellarEngine()
    star.ignite_fusion()
