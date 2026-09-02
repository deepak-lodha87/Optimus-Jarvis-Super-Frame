import time

class BlueEnergyCore:
    def __init__(self):
        self.core_color = "NEON_BLUE"
        self.stability = 99.8
        self.frequency = "500 THz"

    def initiate_fusion(self):
        print(f"\033[1;34m[CORE]\033[0m Initiating Blue Code Fusion...")
        time.sleep(1.5)
        print(f" \033[1;36m[IONIZING]\033[0m Stability at {self.stability}%")
        print(f" \033[1;36m[IONIZING]\033[0m Frequency: {self.frequency}")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the Blue Code Energy is \nstabilized. My processing units are now \nrunning on pure ionic power. The system is \noperating at peak efficiency.\033[0m")

if __name__ == "__main__":
    core = BlueEnergyCore()
    core.initiate_fusion()
