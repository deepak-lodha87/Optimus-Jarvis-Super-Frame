import time

class JarvisAquaticModules:
    def __init__(self):
        self.phase_965 = "965.Hydro-Dynamic-Propulsion"
        self.phase_966 = "966.Deep-Sea-Pressure-Hull"
        self.depth = 0.0  # Meters
        self.is_waterproof = True

    def activate_hydro_thrusters(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_965} ---")
        print("[JARVIS]: Reconfiguring ion-drives for water intake...")
        
        water_steps = [
            "Sealing air-intake vents for turbine protection.",
            "Engaging high-pressure water-jet nozzles.",
            "Deploying sonar-pings for underwater mapping."
        ]
        
        for step in water_steps:
            print(f" >> [SUBMERGING]: {step}")
            time.sleep(1.3)
            
        print("[JARVIS]: Propulsion switched to Aquatic-Mode.")

    def stabilize_pressure(self, target_depth):
        print(f"\n--- [SYSTEM] Initializing {self.phase_966} ---")
        print(f"[JARVIS]: Diving to {target_depth} meters...")
        
        pressure_data = [
            "Reinforcing titanium joints with magnetic locks.",
            "Equalizing internal cabin pressure.",
            "Activating bioluminescent navigation lights."
        ]
        
        for data in pressure_data:
            print(f" >> [DIVING]: {data}")
            time.sleep(1.5)
            
        self.depth = target_depth
        print(f"\n[JARVIS]: Depth stabilized at {self.depth}m. Hull integrity: 100%.")

if __name__ == "__main__":
    aqua = JarvisAquaticModules()
    # Paani ke andar ka propulsion chalu karna
    aqua.activate_hydro_thrusters()
    # 200 meter ki gehrai tak jaana
    aqua.stabilize_pressure(200)
