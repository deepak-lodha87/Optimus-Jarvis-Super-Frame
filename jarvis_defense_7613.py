import time, secrets

class JarvisTacticalDefense:
    def __init__(self):
        self.def_id = f"NAGw-{secrets.token_hex(3).upper()}"
        self.status = "DEFENSE-GRID-ACTIVE"

    def activate_tactical_array(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GRAND-WEAPONRY: TACTICAL DEFENSE (ID: {self.def_id}) ---\033[0m")
        print("\033[1;36m[DEFENSE] Initializing Targeting Sensors and Shield Arrays... \033[0m")
        time.sleep(2)
        
        layers = ["Target-Acquisition", "Laser-Thermal-Lock", "Sonic-Wave-Calibration", "Kinetic-Shield-Sync"]
        for layer in layers:
            print(f" > Layer: {layer:25} | Status: \033[1;32mREADY\033[0m")
            time.sleep(0.7)
            
        print(f"\n\033[1;33m[STATUS] Defense Perimeter Established. No unauthorized access possible.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the perimeter is locked. Every tactical tool and defense mechanism is synced with your neural patterns. We are no longer just building; we are protecting. Our defense is absolute.\033[0m")

if __name__ == "__main__":
    defense = JarvisTacticalDefense()
    defense.activate_tactical_array()
