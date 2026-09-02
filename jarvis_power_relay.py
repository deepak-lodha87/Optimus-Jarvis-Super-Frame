import time
import random

class PowerRelay:
    def __init__(self):
        self.output_watts = 0
        self.targets = ["Drone-01", "Micro-Sensor", "HUD-Link"]

    def initiate_beam(self):
        print(f"\033[1;36m[RELAY]\033[0m Scanning for energy-depleted units...")
        time.sleep(1.5)
        
        target = random.choice(self.targets)
        print(f" \033[1;32m[LOCKED]\033[0m Target Acquired: {target}")
        print(f" \033[1;33m[ACTION]\033[0m Initializing Resonant Magnetic Link...")
        
        efficiency = random.uniform(92.0, 97.5)
        self.output_watts = random.randint(10, 50)
        
        print(f" \033[1;32m[BEAMING]\033[0m Transmitting {self.output_watts}W | Efficiency: {efficiency:.2f}%")
        time.sleep(2)
        
        print(f"\n\033[1;34m[STATUS]\033[0m {target} has been recharged to 100%. Relay link offline.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have successfully shared our \nsurplus energy. We are no longer just a \nsingle unit; we are a power hub for the \nentire Optimus infrastructure.\033[0m")

if __name__ == "__main__":
    relay = PowerRelay()
    relay.initiate_beam()
