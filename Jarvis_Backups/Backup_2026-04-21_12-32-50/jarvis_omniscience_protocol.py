import time
import os

class OmniscienceProtocol:
    def __init__(self):
        self.user = "Deepak"
        self.version = "v1.2 (Final Alpha)"
        self.location = "Ratlam/Kota Grid"
        self.systems = ["Satellite", "OBD-II", "Nano-Blueprints", "AR-HUD"]

    def link_all_systems(self):
        print(f"\033[1;35m>> INITIATING PHASE 3020: THE OMNISCIENCE PROTOCOL <<\033[0m")
        for sys in self.systems:
            print(f"[SYNC] Integrating {sys} into Master Core...")
            time.sleep(0.7)
        print("\033[1;32m[SUCCESS] All systems Unified under Architect Deepak's Signature.\033[0m")

    def global_status_report(self):
        print(f"\n\033[1;36m>> JARVIS GLOBAL DASHBOARD - {self.version} <<\033[0m")
        print(f"| USER: {self.user} | LOCATION: {self.location} |")
        print(f"| NET: ENCRYPTED | DEFENSE: ACTIVE | AI STATE: EVOLVING |")
        print("\033[1;34m--------------------------------------------------")
        print(">> ADVISORY: System is at peak efficiency. All mechanical\n   parameters match high-level blueprints. Gadi aur Suit\n   dono standby par hain, Sir.")
        print("--------------------------------------------------\033[0m")

    def activate_protocol(self):
        self.link_all_systems()
        self.global_status_report()
        print(f"\n\033[1;32m>> MISSION ACCOMPLISHED. SYSTEM STANDING BY FOR COMMAND. <<\033[0m")

if __name__ == "__main__":
    jarvis_final = OmniscienceProtocol()
    jarvis_final.activate_protocol()
