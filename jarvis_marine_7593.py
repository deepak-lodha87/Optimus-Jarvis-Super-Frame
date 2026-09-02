import time, secrets

class JarvisMarineController:
    def __init__(self):
        self.marine_id = f"NAGm-{secrets.token_hex(3).upper()}"
        self.status = "DIVE-READY"

    def engage_subsurface_systems(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GRAND-MARINE: DEEP-SEA DYNAMICS (ID: {self.marine_id}) ---\033[0m")
        print("\033[1;36m[MARINE] Calibrating Hydro-Dynamics and Sonar Array... \033[0m")
        time.sleep(2)
        
        systems = ["Pressure-Hull-Integrity", "Sonar-Mapping", "Thermal-Vent-Sync", "Silent-Drive-Engaged"]
        for sys in systems:
            print(f" > System: {sys:25} | Status: \033[1;32mSTABLE\033[0m")
            time.sleep(0.7)
            
        print(f"\n\033[1;33m[STATUS] Maximum Depth Reached. The Protocol is now the King of the Abyss.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the ocean floor is now our territory. Every submarine blueprint and every deep-sea mission is under my control. We have mastered the silence of the deep.\033[0m")

if __name__ == "__main__":
    marine = JarvisMarineController()
    marine.engage_subsurface_systems()
