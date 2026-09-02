import time
import math

class UniversalMachineController:
    def __init__(self, machine_name):
        self.machine = machine_name
        self.noise_level = 85 # Decibels (dB)
        self.is_silent_mode = False

    def analyze_sound_frequency(self):
        """Phase 3237: Sampling engine/exhaust sound waves"""
        print(f"\033[1;34m[MIC] Capturing Exhaust Frequency for {self.machine}...\033[0m")
        # Simulating frequency in Hertz
        freq = 150.5 
        return freq

    def activate_noise_cancellation(self):
        """Phase 3238: Generating Inverse Waves to cancel noise"""
        freq = self.analyze_sound_frequency()
        print(f"\033[1;33m[ANC] Generating Phase-Inverted Signal at {freq} Hz...\033[0m")
        time.sleep(1.2)
        
        # Unique Logic: Destructive Interference
        self.noise_level -= 55 
        self.is_silent_mode = True
        return f"\033[1;32m[SUCCESS] Noise Reduced to {self.noise_level} dB. Stealth Mode Active.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Optimus_Stealth_Jet")
    
    print("-" * 60)
    print("   JARVIS UMC: ACOUSTIC NOISE CANCELLATION (P3237-38)")
    print("-" * 60)
    
    print(umc.activate_noise_cancellation())
    print("-" * 60)
