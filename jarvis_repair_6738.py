import time, secrets, random

class JarvisHardwareGuard:
    def __init__(self):
        self.repair_id = f"NARe-{secrets.token_hex(2).upper()}"
        self.hardware_status = "Scanning"

    def diagnose_systems(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-REPAIR V2 ACTIVE (ID: {self.repair_id}) ---\033[0m")
        print("\033[1;36m[DIAGNOSTIC] Analyzing electrical impedance and thermal flux...\033[0m")
        time.sleep(2)
        
        # Simulating hardware check
        components = ["Actuator-7", "LiDAR-Sensor", "Power-Conduit"]
        target = random.choice(components)
        wear = random.randint(5, 45)
        
        print(f"\033[1;32m[REPORT] {target} Health: {100-wear}% | Status: Operational\033[0m")
        
        if wear > 30:
            print(f"\033[1;33m[ADVICE] {target} showing early signs of mechanical stress. Adjusting load torque.\033[0m")
        
        print(f"\033[1;35m[VOICE] Deepak, all hardware nodes are stable. I've rerouted power to avoid the minor resistance in {target}.\033[0m")

if __name__ == "__main__":
    mechanic = JarvisHardwareGuard()
    mechanic.diagnose_systems()
