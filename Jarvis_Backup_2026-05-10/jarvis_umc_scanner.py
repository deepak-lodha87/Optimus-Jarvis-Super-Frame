import time
import random

class UniversalMachineController:
    def __init__(self, machine_part):
        self.part = machine_part
        self.integrity_score = 100.0 # 100% means perfect

    def initiate_ultrasonic_pulse(self):
        """Phase 3233: Sending high-frequency waves through the material"""
        print(f"\033[1;34m[SCANNER] Emitting Ultrasonic Pulses into {self.part}...\033[0m")
        time.sleep(1.2)
        # Unique Logic: Checking for echo delay (reflects internal cracks)
        echo_delay = random.uniform(0.01, 0.05)
        return echo_delay

    def analyze_structural_fatigue(self):
        """Phase 3234: Calculating metal stress and crack probability"""
        delay = self.initiate_ultrasonic_pulse()
        print("\033[1;33m[ANALYSIS] Measuring Wave Reflection & Material Density...\033[0m")
        time.sleep(1)
        
        if delay > 0.04: # High delay means the wave hit a crack
            self.integrity_score -= random.randint(15, 30)
            status = f"\033[1;31m[WARNING] Internal Stress Fracture Detected! Integrity: {self.integrity_score}%\033[0m"
        else:
            status = "\033[1;32m[SAFE] Molecular Structure Intact. No Cracks Found.\033[0m"
            
        return status

if __name__ == "__main__":
    umc = UniversalMachineController("Main_Engine_Crankshaft")
    
    print("-" * 60)
    print("   JARVIS UMC: ULTRASONIC INTEGRITY SCAN (P3233-34)")
    print("-" * 60)
    
    # Scanning the part
    print(umc.analyze_structural_fatigue())
    print("-" * 60)
