import time
import random

class UniversalMachineController:
    def __init__(self):
        self.oxygen_level = 100 # %
        self.structural_integrity = 100 # %
        self.encryption_status = "STANDARD"

    def p3463_rebreather_active(self, cabin_sealed):
        if cabin_sealed:
            self.oxygen_level = 98 # Conserving
            return "\033[1;32m[LIFE SUPPORT] Re-breather Active. Recycling CO2 into O2. Survival time: Extended.\033[0m"
        return "[STATUS] External air supply normal."

    def p3464_atomic_scan(self):
        issue_found = random.choice([True, False, False])
        if issue_found:
            self.structural_integrity = 99.8
            return "\033[1;33m[SCAN] Sub-Atomic Fissure detected in Front Axle. Auto-Repair queued.\033[0m"
        return "\033[1;32m[SCAN] Atomic Structure: Stable. Integrity at 100%.\033[0m"

    def p3465_quantum_encryption(self):
        self.encryption_status = "QUANTUM_V2"
        return "\033[1;35m[SECURITY] Neural-Pulse V2 Encryption Locked. Signal is now a ghost to external sniffers.\033[0m"

    def p3466_dust_repulsion(self, dust_layer):
        if dust_layer > 5:
            return "\033[1;34m[SURFACE] Dust level high. Firing Electro-Static Pulse. Surface Cleaned.\033[0m"
        return "[STATUS] Surface is clear."

    def p3467_fluid_recovery(self, leak_detected):
        if leak_detected:
            return "\033[1;31m[RECOVERY] Fluid Leak! Activating Magnetic Scavenge Pumps. 95% Liquid Recovered.\033[0m"
        return "[STATUS] All fluid lines pressurized and secure."

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: SURVIVAL & ATOMIC ANALYSIS (P3463-3467)")
    print("-" * 60)
    
    print(umc.p3463_rebreather_active(True))
    print(umc.p3464_atomic_scan())
    print(umc.p3465_quantum_encryption())
    print(umc.p3466_dust_repulsion(8))
    print(umc.p3467_fluid_recovery(True))
    
    print("-" * 60)
    print("STATUS: Life Support & Atomic Defense Grid Online.")
    print("-" * 60)
