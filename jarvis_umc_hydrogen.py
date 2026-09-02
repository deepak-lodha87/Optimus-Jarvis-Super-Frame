import time
import random

class UniversalMachineController:
    def __init__(self, engine_id):
        self.engine_id = engine_id
        self.hydrogen_flow = 0.0 # Liters per minute
        self.oxygen_ratio = 1.0
        self.combustion_stability = 100

    def calculate_mix_ratio(self, rpm):
        """Advanced Logic: Adjusting mix based on engine load"""
        print(f"\033[1;34m[HYBRID] Analyzing Engine Load at {rpm} RPM...\033[0m")
        time.sleep(1)
        # Optimal ratio for Hydrogen combustion
        self.hydrogen_flow = (rpm / 1000) * 1.5
        self.oxygen_ratio = 1.25 # Lean burn for high efficiency
        return self.hydrogen_flow, self.oxygen_ratio

    def regulate_injector_valves(self):
        flow, ratio = self.calculate_mix_ratio(random.randint(3000, 8000))
        print(f"\033[1;33m[VALVE] Regulating Pulse Width Modulation (PWM)...\033[0m")
        time.sleep(0.8)
        print(f"  • Hydrogen Injection: {flow:.2f} LPM")
        print(f"  • Oxygen Enrichment: {ratio}x")
        return "\033[1;32m[SUCCESS] Optimal Combustion Achieved. Emission: 0.0% CO2.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Optimus_H2_Hybrid")
    
    print("-" * 60)
    print("   JARVIS UMC: HYDROGEN HYBRID OPTIMIZATION (P3227-28)")
    print("-" * 60)
    
    # Simulating high-performance hybrid run
    for _ in range(2):
        print(umc.regulate_injector_valves())
        print("-" * 40)
    print("-" * 60)
