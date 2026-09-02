import time
import random

class OptimusGlobal:
    def __init__(self):
        self.user = "Deepak"
        self.phase_18 = "3018 (Satellite Link-up)"
        self.phase_19 = "3019 (Tactical Defense)"
        self.network = "ENCRYPTED_SAT_LINK"

    def connect_satellite(self):
        print(f"\033[1;35m>> PHASE {self.phase_18}: SEARCHING FOR SATELLITE UPLINK... <<\033[0m")
        time.sleep(1.5)
        satellites = ["GSAT-30", "INSAT-4B", "STARLINK_GLOBAL"]
        active_sat = random.choice(satellites)
        print(f"\033[1;32m[CONNECTED] Linked to {active_sat}. Global Data Access: ENABLED.\033[0m")

    def tactical_defense_grid(self):
        print(f"\n\033[1;36m>> PHASE {self.phase_19}: ACTIVATING TACTICAL DEFENSE GRID <<\033[0m")
        time.sleep(1)
        # Monitoring surroundings via GPS/Satellite
        threat_level = "0.001% (LOW)"
        print(f"[SCAN] Area: Ratlam/Kota | Threat Level: {threat_level}")
        print("\033[1;34m[DEFENSE] Perimeter Secure. No unauthorized interference detected.\033[0m")

    def boot_global(self):
        print(f"\033[1;32m>> SYSTEM ONLINE: GLOBAL NETWORK HANDSHAKE INITIATED. <<\033[0m")
        self.connect_satellite()
        self.tactical_defense_grid()
        print(f"\n\033[1;35m>> STATUS: ARCHITECT DEEPAK, YOU ARE NOW GLOBALLY CONNECTED. <<\033[0m")

if __name__ == "__main__":
    global_jarvis = OptimusGlobal()
    global_jarvis.boot_global()
