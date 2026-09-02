import time

class JarvisLifeSupport:
    def __init__(self):
        self.phase_975 = "975.Closed-Loop-Oxygen-System"
        self.phase_976 = "976.Biometric-Health-Scanner"
        self.oxygen_level = 100.0  # Percentage
        self.heart_rate = 72  # BPM

    def activate_oxygen_supply(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_975} ---")
        print("[JARVIS]: Sealing helmet and activating internal tanks...")
        
        o2_steps = [
            "Recycling exhaled CO2 into breathable oxygen.",
            "Pressurizing the internal cabin-mesh.",
            "Filtering nitrogen-mix for deep-sea or space air."
        ]
        
        for step in o2_steps:
            print(f" >> [AIR-FLOW]: {step}")
            time.sleep(1.2)
            
        print(f"[JARVIS]: Oxygen Supply: Stable. Tank Level: {self.oxygen_level}%")

    def monitor_vitals(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_976} ---")
        print("[JARVIS]: Scanning user's physical condition...")
        
        health_data = [
            "Checking heart-rate and blood-pressure.",
            "Analyzing adrenaline levels for stress-management.",
            "Syncing neural-fatigue with auto-pilot assistance."
        ]
        
        for data in health_data:
            print(f" >> [DIAGNOSIS]: {data}")
            time.sleep(1.4)
            
        print(f"\n[JARVIS]: Health Status: Optimal. Heart Rate: {self.heart_rate} BPM.")

if __name__ == "__main__":
    life = JarvisLifeSupport()
    # Emergency hawa ka intezam
    life.activate_oxygen_supply()
    # Shareer ki halat par nazar rakhna
    life.monitor_vitals()
