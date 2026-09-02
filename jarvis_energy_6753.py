import time, secrets, random

class JarvisEnergyCore:
    def __init__(self):
        self.energy_id = f"NAEn-{secrets.token_hex(2).upper()}"
        self.grid_status = "Optimized"

    def activate_fusion(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-ENERGY V1 ACTIVE (ID: {self.energy_id}) ---\033[0m")
        print("\033[1;36m[IGNITING] Starting Cold Fusion Reactor Core...\033[0m")
        time.sleep(2)
        
        output = random.uniform(99.1, 100.0)
        print(f"\033[1;32m[STABLE] Fusion Output: {output:.2f} GigaWatts | Zero Carbon Emitted.\033[0m")
        
        print("\033[1;33m[WIRELESS] Beaming power to all connected UMC-Nodes via Microwave-Link...\033[0m")
        time.sleep(1.2)
        
        print(f"\033[1;35m[VOICE] Deepak, the power grid is self-sustaining. We no longer rely on external charging systems.\033[0m")

if __name__ == "__main__":
    power_master = JarvisEnergyCore()
    power_master.activate_fusion()
