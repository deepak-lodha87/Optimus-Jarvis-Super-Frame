import time, secrets

class JarvisArcReactor:
    def __init__(self):
        self.reactor_id = f"NAGe-{secrets.token_hex(3).upper()}"
        self.output = "0.0 GW"

    def initiate_core_fusion(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GRAND-ENERGY: ARC REACTOR CORE (ID: {self.reactor_id}) ---\033[0m")
        print("\033[1;36m[ENERGY] Initializing Cold Fusion Sequence... \033[0m")
        time.sleep(2)
        
        stages = ["Magnetic-Containment", "Ionization-Sync", "Plasma-Stabilization", "Power-Grid-Lock"]
        for stage in stages:
            print(f" > Stage: {stage:25} | Status: \033[1;32mONLINE\033[0m")
            time.sleep(0.7)
            
        self.output = "3.5 GW"
        print(f"\n\033[1;33m[STATUS] Stable Energy Flow Detected: {self.output}\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the heart is beating. We have enough energy to power a city, or your entire fleet of suits and drones. The Deepak-Protocol is now self-sustaining. The power of the sun, in our hands.\033[0m")

if __name__ == "__main__":
    energy = JarvisArcReactor()
    energy.initiate_core_fusion()
