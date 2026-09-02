import time

class JarvisHUD:
    def __init__(self):
        self.interface_status = "Standby"
        self.scanning_mode = "Passive"

    def activate_display(self):
        print("Initializing HUD Interface...")
        time.sleep(1)
        self.interface_status = "Active"
        print("Overlaying Tactical Data onto Vision Field...")
        
    def scan_surroundings(self):
        print("Scanning Environment for Objects and Threats...")
        # Simulated Object Recognition
        entities = ["Terrain", "Atmospheric_Pressure", "Target_Alpha"]
        for entity in entities:
            print(f"Tracking: {entity} [LOCKED]")
            time.sleep(0.5)
        return "Scan Complete: Environment Map Updated."

if __name__ == "__main__":
    hud = JarvisHUD()
    hud.activate_display()
    print(hud.scan_surroundings())
