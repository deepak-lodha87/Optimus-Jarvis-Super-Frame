import time
import random

class JarvisEnergyCore:
    def __init__(self):
        self.phase_525 = "525.Fusion-Reactor-Core-Monitoring"
        self.phase_526 = "526.Magnetic-Plasma-Energy-Shielding"
        self.core_temperature = 15000000  # 15 Million Celsius (Fusion Temp)
        self.energy_output = "99.9% Efficiency"

    def monitor_fusion_reactor(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_525} ---")
        time.sleep(1)
        print("[JARVIS]: Syncing with Cold-Fusion Reactor core...")
        
        # एनर्जी आउटपुट और स्टेबिलिटी चेक
        reactor_stats = {
            "Plasma_Stability": "Optimal (Lattice-locked)",
            "Core_Temperature": f"{self.core_temperature} C",
            "Energy_Output": self.energy_output,
            "Fuel_Level": "Hydrogen-Isotope Mix (Stable)"
        }
        
        for metric, value in reactor_stats.items():
            print(f" >> [CORE-DATA]: {metric} -> {value}")
            time.sleep(0.7)
            
        print("[STATUS]: Energy generation is limitless. Systems at full power.")

    def activate_magnetic_shield(self, attack_type):
        print(f"\n--- [SYSTEM] Initializing {self.phase_526} ---")
        time.sleep(1)
        print(f"[JARVIS]: Incoming {attack_type} detected. Calculating magnetic deflection...")
        
        # चुंबकीय ढाल (Magnetic Shield) का लॉजिक
        if attack_type in ["EMP_Pulse", "Laser_Beam", "Plasma_Bolt"]:
            time.sleep(1.2)
            print(f"[ACTION]: Ionizing air to create Plasma-Shield.")
            print(f"[JARVIS]: Magnetic field strength increased to 50 Tesla.")
            print(f"[STATUS]: {attack_type} neutralized by magnetic repulsion.")
        else:
            print("[STATUS]: Standard physical armor sufficient for current threat.")

if __name__ == "__main__":
    jarvis_power = JarvisEnergyCore()
    # Step 1: फ्यूजन रिएक्टर की निगरानी
    jarvis_power.monitor_fusion_reactor()
    # Step 2: चुंबकीय ढाल का परीक्षण
    jarvis_power.activate_magnetic_shield("Laser_Beam")
