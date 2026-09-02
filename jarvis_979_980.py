import time

class JarvisEnergyCore:
    def __init__(self):
        self.phase_979 = "979.Miniature-Fusion-Reactor"
        self.phase_980 = "980.Plasma-Heat-Exchanger"
        self.power_output = "Infinite-Loop"
        self.core_stability = 100.0  # Percentage

    def initiate_fusion(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_979} ---")
        print("[JARVIS]: Igniting hydrogen-plasma core...")
        
        fusion_steps = [
            "Aligning magnetic-containment rings.",
            "Injecting tritium-deuterium fuel mix.",
            "Achieving self-sustaining cold-fusion reaction."
        ]
        
        for step in fusion_steps:
            print(f" >> [IGNITION]: {step}")
            time.sleep(1.2)
            
        print(f"[JARVIS]: Power Generation: {self.power_output}. Energy depletion: 0%.")

    def manage_excess_heat(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_980} ---")
        print("[JARVIS]: Monitoring core temperature spikes...")
        
        vent_steps = [
            "Opening emergency plasma-exhaust ports.",
            "Converting excess thermal energy into kinetic-thrust.",
            "Balancing core-pressure via liquid-helium cooling."
        ]
        
        for step in vent_steps:
            print(f" >> [VENTING]: {step}")
            time.sleep(1.4)
            
        print(f"\n[JARVIS]: Core Stability: {self.core_stability}%. Thermal management optimized.")

if __name__ == "__main__":
    energy = JarvisEnergyCore()
    # Unlimited power chalu karna
    energy.initiate_fusion()
    # Garmi aur pressure ko control karna
    energy.manage_excess_heat()
